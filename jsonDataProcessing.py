# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/11/18 15:39
# File : jsonDataProcessing.py
import numpy as np
import pandas as pd



filepath = "data/crime_classify.json"
df = pd.read_json(filepath,encoding='utf8',lines=True)


#打开文件保存到列表中
lines = open(filepath,encoding='utf8').readlines()

# 训练集大小
TRAIN_SIZE = 0.7
train_num = int(len(lines)*TRAIN_SIZE)

# 打乱
np.random.shuffle(lines)

# 存前面 70%
with open("data/crime_classify_train.json",'w',encoding='utf8') as f:
    for i in range(train_num):
        f.write(lines[i])
f.close()

# 存后面 30% range 左开右闭 不用担心重复
with open("data/crime_classify_test.json",'w',encoding='utf8') as f:
    for i in range(train_num,len(lines)):
        f.write(lines[i])
f.close()
