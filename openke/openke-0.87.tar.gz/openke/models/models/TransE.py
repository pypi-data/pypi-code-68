# coding:utf-8
import tensorflow as tf

from .Model import Model


class TransE(Model):
    r'''
    TransE is the first model to introduce translation-based embedding,
    which interprets relations as the translations operating on entities.
    '''

    def _calc(self, h, t, r):
        h = tf.nn.l2_normalize(h, -1)
        t = tf.nn.l2_normalize(t, -1)
        r = tf.nn.l2_normalize(r, -1)
        return abs(h + r - t)

    def embedding_def(self):
        # Obtaining the initial configuration of the model
        config = self.get_config()
        # Defining required parameters of the model, including embeddings of entities and relations
        self.ent_embeddings = tf.keras.layers.Embedding(config.entTotal, config.hidden_size, name="ent_embeddings")
        self.rel_embeddings = tf.keras.layers.Embedding(config.relTotal, config.hidden_size, name="rel_embeddings")
        self.parameter_lists = {"ent_embeddings": self.ent_embeddings, \
                                "rel_embeddings": self.rel_embeddings}

    def look_up_htr(self, h, t, r):
        return [self.ent_embeddings(h), self.ent_embeddings(t), self.rel_embeddings(r)]

    def loss_def(self):
        # Obtaining the initial configuration of the model
        config = self.get_config()
        # To get positive triples and negative triples for training
        # The shapes of pos_h, pos_t, pos_r are (batch_size, 1)
        # The shapes of neg_h, neg_t, neg_r are (batch_size, negative_ent + negative_rel)
        pos_h, pos_t, pos_r = self.get_positive_instance(in_batch=True)
        neg_h, neg_t, neg_r = self.get_negative_instance(in_batch=True)
        # Embedding entities and relations of triples, e.g. p_h, p_t and p_r are embeddings for positive triples
        p_h, p_t, p_r = self.look_up_htr(pos_h, pos_t, pos_r)
        n_h, n_t, n_r = self.look_up_htr(neg_h, neg_t, neg_r)
        # Calculating score functions for all positive triples and negative triples
        # The shape of _p_score is (batch_size, 1, hidden_size)
        # The shape of _n_score is (batch_size, negative_ent + negative_rel, hidden_size)
        _p_score = self._calc(p_h, p_t, p_r)
        _n_score = self._calc(n_h, n_t, n_r)
        # The shape of p_score is (batch_size, 1, 1)
        # The shape of n_score is (batch_size, negative_ent + negative_rel, 1)
        p_score = tf.reduce_sum(_p_score, -1, keep_dims=True)
        n_score = tf.reduce_sum(_n_score, -1, keep_dims=True)
        # Calculating loss to get what the framework will optimize
        self.loss = tf.reduce_mean(tf.maximum(p_score - n_score + config.margin, 0))

    def predict_def(self):
        predict_h, predict_t, predict_r = self.get_predict_instance()
        predict_h_e, predict_t_e, predict_r_e = self.look_up_htr(predict_h, predict_t, predict_r)
        self.predict = tf.reduce_mean(self._calc(predict_h_e, predict_t_e, predict_r_e), 1, keep_dims=False)
