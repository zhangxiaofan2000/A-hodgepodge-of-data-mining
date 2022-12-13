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
                    para_list.append(parpas[i+1].text)
                except:
                    print("超出索引")
        return para_list
    except :
        return False

import os

def list2txt(lst, name,outputpath):
  try:
    txtFile = f"{outputpath}/{name}.txt"
    with open(txtFile, "w") as file:
      # Write each item in the list to the file on a new line
      for item in lst:
        file.write(str(item) + "\n")
  except Exception as e:
    print(str(e))
    return False
  finally:
    file.close()

def set_wd(filepath):
        try:
            file_list = os.listdir(filepath)
            return file_list
        except:
            print("Error")
            return False


if __name__ == '__main__':
    filepath=r"G:\proprocess\data\test"
    outputpath = r"G:\proprocess\data\output"
    keyword="亿"

    filelist = set_wd(filepath)
    if filelist!=[] and filelist!=False:
        for file in set_wd(filepath):
            try:
                filename = filepath+"\\"+file
                paragraphs = getpara(filename)
                result = findKeywordGetNextParagraphs(paragraphs,keyword)
                if(result!=[] and result!=False):
                    list2txt(result, file,outputpath)
            except Exception as e:
                print("未知的错误"+ file + str(e) )



