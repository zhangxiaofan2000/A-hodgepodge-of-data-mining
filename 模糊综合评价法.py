# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/9/23 20:00
# File : 模糊综合评价法.py
import pandas as pd
import numpy as np

class FuzzyEvaluation():

    def __init__(self):
        self.W=np.array()
        self.R=np.array()
    def M1(self,W,R):
        '''
        模糊合成算子M(∧，∨)
        :param W: 权系数矩阵
        :param R: 评价矩阵
        :return: 模糊评判向量
        '''



if __name__ == '__main__':
    # 提取数据
    df = pd.read_csv(r'.\data\a0572a54-1eb1-4b9f-9c4e-c1980b6364e4_1.csv')

    columns = ['省份', '城市', '河流', '流域', '断面名称', '监测时间', '水质类别', '水温', 'pH', 'pH类别',
           '溶解氧', '溶解氧类别', '高锰酸钾', '高锰酸钾类别', '氨氮', '氨氮类别', '总磷', '总氮', '电导率', '浊度',
           '叶绿素', '藻密度', '站点情况']



