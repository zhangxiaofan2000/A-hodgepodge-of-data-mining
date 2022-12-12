# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/12 21:05
# File : word_proces.py

#-*- coding = utf-8 -*-
import docx
import re

#获取docx⽂档的所有段落 path : 相对路径包含⽂档名称
def getpara(path):
    try :
        docx_temp = docx.Document(path)
    except :
        print("can't open the docx")
        return False
    try :
        docx_para = docx_temp.paragraphs
        print("Succeed getting the para:",path)
        return docx_para
    except :
        print("can't get the ",path," paragraphs")
        return False

#从段落中抽取⽬标段落
def findpara(parpas,keyword):
    try :
        para_list = list()
        pattern = re.compile(keyword)
        for para in parpas :
            match1 = pattern.search(para.text)
            if match1 :
                para_list.append(para.text)
        return para_list
    except :
        return False

#返回有keyword 的 下一段
def findKeywordGetNextParagraphs(parpas,keyword):
    try :
        para_list = list()
        pattern = re.compile(keyword)
        for i,para in enumerate(parpas) :
            match1 = pattern.search(para.text)
            if match1 :
                try:
                    para_list.append(parpas[i+1])
                except:
                    print("超出索引")
        return para_list
    except :
        return False

import os

def list2txt(lst, name):
    try:
        fp = open("{}.txt".format(name), "w")
        for item in lst:
            fp.write(item)
            fp.write("\n")
    except:
        return False
    finally:
        fp.close()

def set_wd(filepath):
        try:
            os.chdir(filepath)
            file_list = os.listdir(filepath)
            return file_list
        except:
            print("Error")
            return False


if __name__ == '__main__':
    filepath="文件路径"
    keyword="亿"

    filelist = set_wd(filepath)
    if filelist!=[] and filelist!=False:
        for file in set_wd(filepath):
            try:
                paragraphs = getpara(file)
                result = findKeywordGetNextParagraphs(paragraphs,keyword)
                if(result!=[]):
                    list2txt(result, file)
            except Exception as e:
                print("未知的错误"+ file + str(e) )



