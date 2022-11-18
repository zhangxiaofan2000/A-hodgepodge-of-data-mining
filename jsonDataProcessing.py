# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/11/18 15:39
# File : jsonDataProcessing.py


import pandas as pd

import json
import pandas as pd
from pandas import DataFrame

'''加逗号分隔符，并且使json文件变为列表形式'''

def add_delimiter(input_data, real_input):
    '''
    :param input_data: 原始输入json文件
    :param new_input: 加完分隔符的实际输入json文件
    :return: 无
    '''
    with open(input_data, 'r', encoding="utf-8") as fr:
        with open(real_input, 'w', encoding="utf-8") as fw:
            for line in fr:  # 读取input_data中每一行
                    fw.writelines(line.strip("\n") + ',' + "\n")  # 变为"},"
                    fw.writelines(line)
    with open(real_input, 'r+', encoding="utf-8") as fs:
        content = fs.read()  # 读取real_input中的所有内容
        fs.seek(0)  # 指针指到文件开头
        fs.write("[")
        fs.write(content)
        fs.seek(0, 2)  # 指针指到末尾，偏移量为0
        fs.write("]")

input_data = "data/crime_classify.json"
real_input = "data/crime_classify2.json"
add_delimiter(input_data, real_input)

'''json文件转换为csv文件'''

#
# def to_csv(real_input, csv_file):
#     '''
#     :param real_input: 加完分隔符的实际输入json文件
#     :param csv_file: 转换后的csv文件
#     :return: 无
#     '''
#     data = {  # 每一个需要的标签作为key，空列表作为值存入新定义的data字典
#         'disease_name': [],
#         'disease_subject': [],
#         'question': [],
#         'treatment': [],
#         'symptom': []
#     }
#     with open(real_input, "r", encoding="utf-8") as fr:
#         dicts = json.load(fr)  # 注意这里一定是用json.load拿到每一个字典而不是json.loads
#         for dict in dicts:  # 遍历每一个字典dict
#             data['disease_name'].append(dict['disease_name'])
#             data['disease_subject'].append(dict['disease_subject'])
#             data['question'].append(dict["ask_dict"]["question"])  # 嵌套字典索引
#             data['treatment'].append(dict["treatment"])
#             data['symptom'].append(dict["symptom"])
#         output = DataFrame(data, columns=["disease_name", "disease_subject", "question", "treatment", "symptom"])
#         output.to_csv(csv_file, header=True, index=False)  # 用pandas写入csv
#
#
# csv_file = "csv_file.csv"
# to_csv(real_input, csv_file)
#


def add_d(filepath):
    # file.txt中存的是我需要批量读取的txt的绝对路径
    lines = open(filepath).readlines()

    with open(filepath) as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            lines[i] = "change_str" + lines[i].strip() + "change_str" + "\n"
    with open(filepath, "w") as f2:
        f2.writelines(lines)
    with open(filepath, "r+") as f3:
        content = f2.read()
        f3.seek(0, 0)
        str_ = "[\n"
        f3.write(str_ + content)
    with open(filepath, "r+") as f3:
        content = f2.read()
        f3.seek(0, 0)
        str_ = "[\n"
        f3.write(str_ + content)


# filepath = "data/crime_classify.json"
# # filepath = "http://114.55.141.197:8088/AndroidItem/Android/getRecordNewByDevSerialNumberAndNum?dev=10093&num=10000"
# df = pd.read_json(filepath,encoding='utf8')
df = pd.read_json(input_data,encoding='utf8')