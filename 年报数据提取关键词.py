# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/9/29 17:37
# File : 年报数据提取关键词.py

'''
    #利用python读取word文档，先读取段落
'''
import re
import os
from docx import Document
import difflib
from tqdm import tqdm
import pandas as pd
import concurrent.futures

def word_find(file_name,keyword,keyword2_list):
    try:
        #打开word文档
        document = Document(f'{path}\{file_name}')

        #获取所有段落
        all_paragraphs = document.paragraphs

        #是列表就开始循环读取
        all_list = []

        # 虚拟变量
        variable = 0

        #查找字段
        for paragraph in all_paragraphs:
            str1 = paragraph.text
            if str1.find(keyword) != -1:
                all_list.append(len(re.findall(keyword, str1)))


        # 如果查到区块链，则查找是否实施
        if all_list!=[]:
            for keyword2 in keyword2_list:
                for paragraph in all_paragraphs:
                    str1 = paragraph.text
                    if str1.find(keyword2) != -1:
                        variable = 1
                        break
    except:
        all_list =[]
        variable =[]
        print(file_name)
    print(file_name)
    return sum(all_list),variable

def filename_handle(filename):
    if len(filename)==16:
        return filename[0:6],filename[7:11]
    else:
        list1 = filename.split('-')
        return list1[0],list1[2][0:4],list1[1]



if __name__ == '__main__':

    path = 'G:\proprocess\data\深圳交易所A股'
    key_word = '区块链'
    key_word2 = ['使用区块链','实施区块链','应用区块链','制定区块链','计划区块链','布置区块链','架构区块链']
    output_path = 'G:\proprocess\data\output'


    result = pd.DataFrame()
    key_word = [key_word for _ in range(len(os.listdir(path)))]
    key_word2 = [key_word2 for _ in range(len(os.listdir(path)))]

    args_list = list(zip(os.listdir(path), key_word, key_word2))
    with concurrent.futures.ThreadPoolExecutor() as executor:

        results = executor.map(word_find,os.listdir(path),key_word,key_word2)


    print('ok')
    # for file_name in tqdm(os.listdir(path)):
    #     try :
    #         count,var = word_find(file_name, key_word,key_word2)
    #
    #         if len(file_name)==16:
    #             index,col = file_name[0:6],file_name[7:11]
    #             result.loc[index,col] = count
    #             result.loc[index, '虚拟变量'] = var
    #         else:
    #             list1 = file_name.split('-')
    #             index, col = list1[0],list1[2][0:4]
    #             EnterpriseName = list1[1]
    #             result.loc[index, col] = count
    #             result.loc[index, '企业名称'] = EnterpriseName
    #             result.loc[index, '虚拟变量'] = var
    #     except:
    #         continue
    # result.fillna(0)
    # result.to_excel(output_path+'\深圳交易所A股.xlsx')



#
#
# path = 'G:\proprocess\data\上海交易所A股'
# key_word = '区块链'
# key_word2 = ['使用区块链','实施区块链','应用区块链','制定区块链','计划区块链','布置区块链','架构区块链']
# output_path = 'G:\proprocess\data\output'
#
#
# result = pd.DataFrame()
#
#
# def filename_handle(filename):
#     if len(filename)==16:
#         return file_name[0:6],file_name[7:11]
#     else:
#         list1 = filename.split('-')
#         return list1[0],list1[2][0:4],list1[1]
#
#
# for file_name in tqdm(os.listdir(path)):
#     try:
#         count, var = word_find(file_name, key_word, key_word2)
#
#         if len(file_name) == 16:
#             index, col = file_name[0:6], file_name[7:11]
#             result.loc[index, col] = count
#             result.loc[index, '虚拟变量'] = var
#         else:
#             list1 = file_name.split('-')
#             index, col = list1[0], list1[2][0:4]
#             EnterpriseName = list1[1]
#             result.loc[index, col] = count
#             result.loc[index, '企业名称'] = EnterpriseName
#             result.loc[index, '虚拟变量'] = var
#     except:
#         continue
#
# result.fillna(0)
# result.to_excel(output_path+'\上海交易所A股.xlsx')