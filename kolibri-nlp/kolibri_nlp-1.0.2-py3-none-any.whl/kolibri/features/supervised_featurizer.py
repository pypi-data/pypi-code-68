import logging
import os
import re, joblib
from typing import Any, Dict, List, Optional, Text
from kolibri.features.features import Features
from sklearn.feature_extraction.text import CountVectorizer
from kolibri.features.supervised_weigthing import *
from string import punctuation
logger = logging.getLogger(__name__)


class CBTWFeaturizer(Features):
    """Bag of words featurizer

    Creates bag-of-words representation of intent features
    using sklearn's `CountVectorizer`.
    All tokens which consist only of digits (e.g. 123 and 99
    but not ab12d) will be represented by a single feature."""

    name = "tf_cbtw_featurizer"

    provides = ["text_features"]

    requires = ["tokens"]

    defaults = {
        # the parameters are taken from
        # sklearn's CountVectorizer

        # regular expression for tokens
        "token_pattern": r'(?u)\b\w\w+\b',

        # remove accents during the preprocessing step
        "strip_accents": None,  # {'ascii', 'unicode', None}

        # list of stop words
        "stop_words": None,  # string {'en'}, list, or None (default)

        #term weighting algorithm
        "weight_algorithm": "chi2",

        "reduce_algorithm": "max",
        # set range of ngrams to be extracted
        "min_ngram": 1,  # int
        "max_ngram": 1,  # int
        # min document frequency of a word to add to vocabulary
        # float - the parameter represents a proportion of documents
        # integer - absolute counts
        "min_df": 7,  # float in range [0.0, 1.0] or int

        # max document frequency of a word to add to vocabulary
        # float - the parameter represents a proportion of documents
        # integer - absolute counts
        "max_df": 0.7,  # float in range [0.0, 1.0] or int

        # limit vocabulary size
        "max_features": 5000,  # int or None

        # if convert all characters to lowercase
        "lowercase": False,  # bool
        "use_bigram_model": False

    }

    @classmethod
    def required_packages(cls):
        # type: () -> List[Text]
        return ["sklearn"]

    def _load_count_vect_params(self):
        # regular expression for tokens
        self.token_pattern = self.component_config['token_pattern']

        # remove accents during the preprocessing step
        self.strip_accents = self.component_config['strip_accents']

        # list of stop words
        self.stop_words = self.component_config['stop_words']

        # min number of word occurancies in the document to add to vocabulary
        self.min_df = self.component_config['min_df']

        # max number (fraction if float) of word occurancies
        # in the document to add to vocabulary
        self.max_df = self.component_config['max_df']

        # set ngram range
        self.min_ngram = self.component_config['min_ngram']
        self.max_ngram = self.component_config['max_ngram']

        # limit vocabulary size
        self.max_features = self.component_config['max_features']

        # if convert all characters to lowercase
        self.lowercase = self.component_config['lowercase']


    def __init__(self, component_config=None):
        """Construct a new count vectorizer using the sklearn framework."""

        super(CBTWFeaturizer, self).__init__(component_config)

        # parameters for sklearn's CountVectorizer
        self._load_count_vect_params()
        self.use_bigram_model=self.component_config["use_bigram_model"]
        # declare class instance for CountVectorizer
        self.vectorizer = None
        self.count_vect=None
    def _identity_tokenizer(self, text):
        return text

    @staticmethod
    def _get_document_text(document, lowercase):
        if document.nlp_doc and len(document.nlp_doc.tokens)>0:  # if lemmatize is possible
            if document.nlp_doc.tokens[0].lemma:
                tokens = [t for t in document.nlp_doc.tokens if not t.is_stopword and t.text not in punctuation]
                if lowercase:
                    return [t.lemma.lower() if t.abstract is None else t.abstract for t in tokens]
                return [t.lemma if t.abstract is not None else t.abstract for t in tokens]
            elif document.nlp_doc.tokens[0].stem:
                tokens = [t for t in document.nlp_doc.tokens if not t.is_stopword and t.text not in punctuation]
                if lowercase:
                    return [t.stem.lower() if t.abstract is None else t.abstract for t in tokens]
                return [t.stem if t.abstract is None else t.abstract for t in tokens]
        elif document.tokens:  # if directly tokens is provided
            tokens = [t for t in document.tokens if not t.is_stopword and t.text not in punctuation]
            if lowercase:
                return [t.text.lower() if t.abstract is None else t.abstract for t in tokens]
            return [t.text if t.abstract is None else t.abstract for t in tokens]
        else:
            return document.text

    def train(self, training_data, cfg=None, **kwargs):
        """Take parameters from config and
            construct a new tfidf vectorizer using the sklearn framework."""



        lem_exs = [self._get_document_text(example, self.lowercase)
                   for example in training_data.training_examples]

        y = [str(e.target)
                  for e in training_data.training_examples]

        self.count_vect = CountVectorizer(token_pattern=self.token_pattern,
                                    strip_accents=self.strip_accents,
                                    lowercase=False,
                                    min_df=self.min_df, max_df=self.max_df,
                                    tokenizer=self._identity_tokenizer)

        weighting=self.component_config["weight_algorithm"]
        reduction=self.component_config["reduce_algorithm"]

        self.vectorizer=SupervisedTermWeights(weighting=weighting,
                                              reduce=reduction)

        try:
            X = self.count_vect.fit_transform(lem_exs).toarray()
            X = self.vectorizer.fit_transform(X, y)
        except ValueError as e:
            self.vectorizer = None
            return

        for i, example in enumerate(training_data.training_examples):
            # create bag for each example
            example.text_features=self._combine_with_existing_features(example,
                                                                  X[i])

    def process(self, document, **kwargs):

        if self.vectorizer is None:
            logger.error("There is no trained CountVectorizer: "
                         "component is either not trained or "
                         "didn't receive enough training data")
        else:
            document_text = self._get_document_text(document, self.lowercase)
            bag=self.count_vect.transform([document_text])
            bag = self.vectorizer.transform(bag).toarray().squeeze()
            document.text_features=self._combine_with_existing_features(document,
                                                                  bag)

    def persist(self, model_dir):
        # type: (Text) -> Dict[Text, Any]
        """Persist this model into the passed directory.
        Returns the metadata necessary to load the model again."""

        featurizer_file = os.path.join(model_dir, self.name + ".pkl")
        joblib.dump(self, featurizer_file)
        return {"featurizer_file": self.name + ".pkl"}

    @classmethod
    def load(cls,
             model_dir=None,
             model_metadata=None,
             cached_component=None,
             **kwargs
             ):


        meta = model_metadata.for_component(cls.name)

        if model_dir and meta.get("featurizer_file"):
            file_name = meta.get("featurizer_file")
            featurizer_file = os.path.join(model_dir, file_name)
            return joblib.load(featurizer_file)
        else:
            logger.warning("Failed to load featurizer. Maybe path {} "
                           "doesn't exist".format(os.path.abspath(model_dir)))
            return CBTWFeaturizer(meta)
