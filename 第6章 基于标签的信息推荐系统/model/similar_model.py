#coding:utf-8

from gensim import corpora, models, similarities
import pickle
import logging
from gensim import utils
import os
import sys
import numpy as np
import scipy
# from gensim import matutils
# from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity

data_dir = os.path.join(os.getcwd(), 'data')
logger = logging.getLogger('text_similar')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class TextSimilar(utils.SaveLoad):
    def __init__(self):
        self.conf = {}

    def _preprocess(self):
        documents = [doc for doc in open(self.fname) if len(doc)>0]
        docs = [d.split() for d in documents]
        pickle.dump(docs, open(self.conf['fname_docs'], 'wb'))
        dictionary = corpora.Dictionary(docs)
        dictionary.save(self.conf['fname_dict'])
        corpus = [dictionary.doc2bow(doc) for doc in docs]
        corpora.MmCorpus.serialize(self.conf['fname_corpus'], corpus)

        return docs, dictionary, corpus

    def _generate_conf(self):
        fname = self.fname[self.fname.rfind('/') + 1:]
        self.conf['fname_docs']   = '%s.docs' % fname
        self.conf['fname_dict']   = '%s.dict' % fname
        self.conf['fname_corpus'] = '%s.mm' % fname

    def train(self, fname, is_pre=True, method='lsi', **params):
        self.fname = fname
        self.method = method
        self._generate_conf()
        if is_pre:
            self.docs, self.dictionary, corpus = self._preprocess()
        else:
            self.docs = pickle.load(open(self.conf['fname_docs']))
            self.dictionary = corpora.Dictionary.load(self.conf['fname_dict'])
            corpus = corpora.MmCorpus(self.conf['fname_corpus'])

        if params is None:
            params = {}

        logger.info("training TF-IDF model")
        self.tfidf = models.TfidfModel(corpus, id2word=self.dictionary)
        corpus_tfidf = self.tfidf[corpus]

        if method == 'lsi':
            logger.info("training LSI model")
            self.lsi = models.LsiModel(corpus_tfidf, id2word=self.dictionary, **params)
            self.similar_index = similarities.MatrixSimilarity(self.lsi[corpus_tfidf])
            self.para = self.lsi[corpus_tfidf]
        elif method == 'lda_tfidf':
            logger.info("training LDA model")
            self.lda = models.LdaMulticore(corpus_tfidf, id2word=self.dictionary, workers=8, **params)
            self.similar_index = similarities.MatrixSimilarity(self.lda[corpus_tfidf])
            self.para = self.lda[corpus_tfidf]
        elif method == 'lda':
            logger.info("training LDA model")
            self.lda = models.LdaMulticore(corpus, id2word=self.dictionary, workers=8, **params)
            self.similar_index = similarities.MatrixSimilarity(self.lda[corpus])
            self.para = self.lda[corpus]
        else:
            msg = "unknown semantic method %s" % method
            logger.error(msg)
            raise NotImplementedError(msg)
        self.corpus = corpus
            
    def doc2vec(self, doc):
        bow = self.dictionary.doc2bow(doc.split())
        if self.method == 'lsi':
            return self.lsi[self.tfidf[bow]]
        elif self.method == 'lda':
            return self.lda[bow]
        elif self.method == 'lda_tfidf':
            return self.lda[self.tfidf[bow]]


    def find_similar(self, doc, n=10):
        vec = self.doc2vec(doc)
        sims = self.similar_index[vec]
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        for elem in sims[:n]:
            idx, value = elem
            print(' '.join(self.docs[idx]), value)

    def add_doc(self,words_with_space):
        try:
            doc1 = words_with_space.split()
            corpus1 = [self.dictionary.doc2bow(doc1)]
            self._generate_conf()
            self.docs.append(doc1)
            pickle.dump(self.docs, open(self.conf['fname_docs'], 'wb'))
            self.dictionary.add_documents([doc1])
            self.dictionary.save(self.conf['fname_dict'])
            
            self.corpus.append(self.dictionary.doc2bow(doc1))
            corpora.MmCorpus.serialize(self.conf['fname_corpus'], self.corpus)
            self.save()
        except Exception as e:
            logger.error(e, exc_info=True)
            return 1
        
        return 0
