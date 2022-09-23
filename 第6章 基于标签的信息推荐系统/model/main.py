#!/usr/bin/python
#coding:utf-8

import jieba
import jieba.analyse
import collections
import gensim
from gensim import corpora, models,similarities
from gensim.models import Word2Vec
import util_tool as util
import time
import jieba.posseg as pseg
import pymysql
from flask import Flask,jsonify,Response,request
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import csv
import json
from similar_model import TextSimilar
import os
import pickle
import logging
import re


app = Flask(__name__)

data_dir = os.path.join(os.getcwd(), 'data')
work_dir = os.path.join(os.getcwd(), 'model', os.path.basename(__file__).rstrip('.py'))


logger = logging.getLogger('TagExtractor')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def remove_punc(line_sentence):
    multi_version = re.compile("-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-")
    punctuation = re.compile("[-~!@#$%^&*()_+`=\[\]\\\\\n\\t{\}\\\r|;':,./<>?·！@#￥%……&*（）——+【】▋、；‘：“”，。、《》？「『」』]")
    line = multi_version.sub(r"\2", line_sentence)
    line = punctuation.sub(' ', line_sentence)
    return line

class TagExtractor(metaclass=Singleton):
    pass

    def __init__(self):
        stop_word_file = "stopwords.txt"
        jieba.analyse.set_stop_words(stop_word_file)
        self.stop_words_set = self.get_stop_words_set(stop_word_file)

        self.initVariable()

    def initVariable(self):
        content_list = []
        article_ids = []
        
        fname = data_dir + '/new_article.txt'
        num_topics = 30
        method = 'lsi'
        
        article_ids = util.get_file_list(data_dir+"/new_article_ids.txt")
        if article_ids == None:
            article_ids = []
            print("begin conn sql")
            with open("news_list.csv") as file:
                reader = csv.reader(file)
                news_list = list(reader)
            counter = 0
            for row in news_list:
                content = row[2]
                title = row[1]
                
                if content is None: continue
                content = remove_punc(content)
                wordlist = jieba.analyse.textrank(title+" "+content.strip(), withWeight=False)
        
                if len(wordlist)<1: continue
                content_list.append(" ".join(wordlist))
                article_ids.append(row[0])
                counter += 1
                if counter %200 ==0: print("process news count:",str(counter))
                    
            util.writeList2File(data_dir+"/new_article_ids.txt",article_ids)
            util.writeList2File(fname, content_list)

            self.ts = TextSimilar()
            self.ts.train(fname, method=method ,num_topics=num_topics, is_pre=True)
            self.ts.save(method)
            self.article_ids = article_ids

        else:
            print("begin generate matrix")
            self.ts = TextSimilar().load(method)
            self.article_ids = article_ids
    
    

    def get_stop_words_set(self,file_name):
        retList = []
        with open(file_name,'r',encoding = 'utf-8') as file:
            retList = set([line.strip() for line in file])
        return retList


    def doc_sims(self,keys,numDocs):
        if self.ts.dictionary == None or len(self.ts.dictionary)<=0: return None

        row = keys.split(',')#['互联网','工业','企业','数据','生产','智能','制造业','平台','技术','物流']

        tl_bow = self.ts.dictionary.doc2bow(row)
        tl_lsi = self.ts.lsi[tl_bow]
        sims = self.ts.similar_index[tl_lsi]
        sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
        top_docs = (sort_sims[0:numDocs])
        return top_docs
    
    
    
    def get_article_tag(self,article_id):
        if article_id not in self.article_ids: return ""
        print(len(self.article_ids))
        print(len(self.ts.docs))
        idx = list(self.article_ids).index(article_id)
        print(idx)
        lst = self.ts.docs[idx]
#        lst1 = self.ts.docs[idx]
#        lst2 = self.ts.docs[idx+1]
#        print(self.ts.calculate_similar(" ".join(lst1)," ".join(lst2)))
        return ",".join(lst)

    def add_doc(self,aid,title,content):
        if aid == None or len(aid)<=1: return 1
        if content == None or len(content)<=1: return 1
        
        if aid in self.article_ids:
            return 2

        content = content.replace("\r\n"," ")
        content = content.replace("\r"," ")
        content = content.replace("\n"," ")
        content = content.replace("\t","    ")
        
        content = title+" "+content.strip()
        wordlist = jieba.analyse.textrank(content, withWeight=True)
        tmp_list =[]
        for w,x in wordlist:
            if len(w)<1:
                continue
            tmp_list.append(w)
        if len(tmp_list)<=0:
            return 3
        content_words = [term for term in tmp_list if str(term) not in self.stop_words_set]
        if len(content_words)<1:
            return 4
        

        ret = self.ts.add_doc(" ".join(content_words))
        if str(ret) == '0':
            self.article_ids.append(aid)
            util.writeList2File(data_dir + "/new_article_ids.txt",[aid],'a')
            util.writeList2File(data_dir + "/new_article.txt",[" ".join(content_words)],'a')

#             self.ts.save("lsi")
        else:
            return 5

        print(content_words)
        return 0



@app.route('/', methods=['GET'])
def index():
    return "works"

@app.route('/api/v1.0/doctag/<articleid>', methods=['GET'])
def doctag(articleid):
    tager = TagExtractor()
    return tager.get_article_tag(articleid)

@app.route('/api/v1.0/getsims/<int:count>/<keywords>', methods=['GET'])
def getsims(count,keywords):
    tager = TagExtractor()
    
    first10 = tager.doc_sims(keywords,count)
    article_ids = list(tager.article_ids)
    result_ids = []
    for s in first10:
        result_ids.append(article_ids[s[0]])

    return jsonify({'articleids': ",".join(result_ids)})

@app.route('/api/v1.0/add_doc/<aid>', methods=['GET', 'POST'])
def add_article(aid):
    content_json = request.get_json()
    print(content_json)
    title = content_json['title']
    content = content_json['content']
    
    print(aid,title,content)

    tager = TagExtractor()
    ret = tager.add_doc(aid,title,content)
    
    return jsonify({'ret': ret})

           
if __name__ == '__main__':
    tager = TagExtractor()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)  #flask默认的端口
    print("use http://localhost:5000 access API")
    print("Get similar articles via tags demo: http://localhost:5000/api/v1.0/getsims/10/互联网 工业 企业 数据 生产 智能 制造业 平台 技术 物流")
    print("Get article tags via article id: http://localhost:5000/api/v1.0/doctag/70030021749")

    IOLoop.instance().start()

