"""
CorpusReader structured for corpora that contain one instance on each row.
This CorpusReader is specifically used for the Subjectivity Dataset and the
Sentence Polarity Dataset.
- Subjectivity Dataset information -
Authors: Bo Pang and Lillian Lee.
Url: http://www.cs.cornell.edu/people/pabo/movie-review-data
Distributed with permission.
Related papers:
- Bo Pang and Lillian Lee. "A Sentimental Education: Sentiment Analysis Using
    Subjectivity Summarization Based on Minimum Cuts". Proceedings of the ACL,
    2004.
- Sentence Polarity Dataset information -
Authors: Bo Pang and Lillian Lee.
Url: http://www.cs.cornell.edu/people/pabo/movie-review-data
Related papers:
- Bo Pang and Lillian Lee. "Seeing stars: Exploiting class relationships for
    sentiment categorization with respect to rating scales". Proceedings of the
    ACL, 2005.
"""
from six import string_types

#from nltk.dataset.reader.api import *
from kolibri.dataset.utils import concat
from kolibri.dataset.corpusreader import CategorizedCorpusReader, CorpusReader, StreamBackedCorpusView
#from KOLIBRI.Preprocessing.Tokenizer import WhitespaceTokenizer

class CategorizedSentencesCorpusReader(CategorizedCorpusReader, CorpusReader):
    """
    A reader for corpora in which each row represents a single instance, mainly
    a sentence. Istances are divided into categories based on their file identifiers
    (see CategorizedCorpusReader).
    Since many corpora allow rows that contain more than one sentence, it is
    possible to specify a sentence tokenizer to retrieve all sentences instead
    than all rows.
    Examples using the Subjectivity Dataset:
    ['television', 'made', 'him', 'famous', ',', 'but', 'his', 'biggest', 'hits',
    'happened', 'off', 'screen', '.']
    """

    CorpusView = StreamBackedCorpusView

    def __init__(
        self,
        root,
        fileids,
        word_tokenizer=None,#WhitespaceTokenizer(),
        sent_tokenizer=None,
        encoding='utf8',
        **kwargs
    ):
        """
        :param root: The root directory for the dataset.
        :param fileids: a list or regexp specifying the fileids in the dataset.
        :param word_tokenizer: a tokenizer for breaking sentences or paragraphs
            into words. Default: `WhitespaceTokenizer`
        :param sent_tokenizer: a tokenizer for breaking paragraphs into sentences.
        :param encoding: the encoding that should be used to read the dataset.
        :param kwargs: additional parameters passed to CategorizedCorpusReader.
        """

        CorpusReader.__init__(self, root, fileids, encoding)
        CategorizedCorpusReader.__init__(self, kwargs)
        self._word_tokenizer = word_tokenizer
        self._sent_tokenizer = sent_tokenizer

    def _resolve(self, fileids, categories):
        if fileids is not None and categories is not None:
            raise ValueError('Specify fileids or categories, not both')
        if categories is not None:
            return self.fileids(categories)
        else:
            return fileids

    def raw(self, fileids=None, categories=None):
        """
        :param fileids: a list or regexp specifying the fileids that have to be
            returned as a raw string.
        :param categories: a list specifying the categories whose files have to
            be returned as a raw string.
        :return: the given file(s) as a single string.
        :rtype: str
        """
        fileids = self._resolve(fileids, categories)
        if fileids is None:
            fileids = self._fileids
        elif isinstance(fileids, string_types):
            fileids = [fileids]
        return concat([self.open(f).read() for f in fileids])

    def readme(self):
        """
        Return the contents of the dataset Readme.txt file.
        """
        return self.open("README").read()

    def sents(self, fileids=None, categories=None):
        """
        Return all sentences in the dataset or in the specified file(s).
        :param fileids: a list or regexp specifying the ids of the files whose
            sentences have to be returned.
        :param categories: a list specifying the categories whose sentences have
            to be returned.
        :return: the given file(s) as a list of sentences.
            Each sentence is tokenized using the specified word_tokenizer.
        :rtype: list(list(str))
        """
        fileids = self._resolve(fileids, categories)
        if fileids is None:
            fileids = self._fileids
        elif isinstance(fileids, string_types):
            fileids = [fileids]
        return concat(
            [
                self.CorpusView(path, self._read_sent_block, encoding=enc)
                for (path, enc, fileid) in self.abspaths(fileids, True, True)
            ]
        )

    def words(self, fileids=None, categories=None):
        """
        Return all words and punctuation symbols in the dataset or in the specified
        file(s).
        :param fileids: a list or regexp specifying the ids of the files whose
            words have to be returned.
        :param categories: a list specifying the categories whose words have to
            be returned.
        :return: the given file(s) as a list of words and punctuation symbols.
        :rtype: list(str)
        """
        fileids = self._resolve(fileids, categories)
        if fileids is None:
            fileids = self._fileids
        elif isinstance(fileids, string_types):
            fileids = [fileids]
        return concat(
            [
                self.CorpusView(path, self._read_word_block, encoding=enc)
                for (path, enc, fileid) in self.abspaths(fileids, True, True)
            ]
        )

    def _read_sent_block(self, stream):
        sents = []
        for i in range(20):  # Read 20 lines at a time.
            line = stream.readline()
            if not line:
                continue
            if self._sent_tokenizer:
                sents.extend(
                    [
                        self._word_tokenizer.tokenize(sent)
                        for sent in self._sent_tokenizer.tokenize(line)
                    ]
                )
            else:
                sents.append(self._word_tokenizer.tokenize(line))
        return sents

    def _read_word_block(self, stream):
        words = []
        for sent in self._read_sent_block(stream):
            words.extend(sent)
        return words