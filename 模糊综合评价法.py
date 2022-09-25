# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/9/23 20:00
# File : 模糊综合评价法.py
import pandas as pd
import numpy as np

class FuzzyEvaluation():

    # def __init__(self):

        # self.W=np.zeros((1,1))
        # self.R=np.zeros((1,1))
    def M1(self,W,R):
        '''
        模糊合成算子M(∧，∨)
        :param W: 权系数矩阵
        :param R: 评价矩阵
        :return: 模糊评判向量
        '''
        row = 1
        col = R.shape[1]
        S = np.zeros((row,col))
        for j in range(R.shape[1]):
            sj=0
            for i in range(R.shape[0]):
                si = min(W[:,i],R[i,j])
                sj = max(si,sj)
            S[:,j] = sj

        return S
    def M2(self,W,R):
        '''
        模糊合成算子M(·，∨)
        :param W: 权系数矩阵
        :param R: 评价矩阵
        :return: 模糊评判向量
        '''
        row = 1
        col = R.shape[1]
        S = np.zeros((row,col))
        for j in range(R.shape[1]):
            sj=0
            for i in range(R.shape[0]):
                sj = max(W[:,i]*R[i,j],sj)
            S[:,j] = sj

        return S

    def M3(self,W,R):
        '''
        模糊合成算子M(∧，⊕)
        :param W: 权系数矩阵
        :param R: 评价矩阵
        :return: 模糊评判向量
        '''
        row = 1
        col = R.shape[1]
        S = np.zeros((row,col))
        for j in range(R.shape[1]):
            sj=0
            for i in range(R.shape[0]):
                si = min(W[:, i], R[i, j])
                sj = min(1,si+sj)
            S[:,j] = sj

        return S


    def M4(self,W,R):
        '''
        模糊合成算子M(·，⊕)
        :param W: 权系数矩阵
        :param R: 评价矩阵
        :return: 模糊评判向量
        '''
        row = 1
        col = R.shape[1]
        S = np.zeros((row,col))
        for j in range(R.shape[1]):
            sj=0
            for i in range(R.shape[0]):
                si = W[:, i]* R[i, j]
                sj = min(1,si+sj)
            S[:,j] = sj

        return S



    def S1(self,S):
        '''
        最大隶属原则
        对评判向量S 分析做综合评论
        :param S:
        :return:
        '''
        return max(S)


    def S2(self,S,k):
        '''
        加权平均原则
        :param S:评判向量S
        :param k:待定系数
        :return:
        '''

        return sum(W*10*S**k)/sum(S**k)


def ViewMissingValues():
    '''
    查看空值数量
    :return:
    '''
    df = pd.read_csv(r'.\data\a0572a54-1eb1-4b9f-9c4e-c1980b6364e4_1.csv')

    all_columns = ['省份', '城市', '河流', '流域', '断面名称', '监测时间', '水质类别', '水温', 'pH',
                   '溶解氧', '高锰酸钾', '氨氮', '总磷', '总氮', '电导率', '浊度',
                   '叶绿素', '藻密度']
    data = df[all_columns]
    print(data[(data['水质类别'] != '-3') & (data['水质类别'] != '-1')].isnull().sum())
    return

if __name__ == '__main__':
    # 读取数据
    df = pd.read_csv(r'.\data\a0572a54-1eb1-4b9f-9c4e-c1980b6364e4_1.csv')

    columns  = ['省份', '城市', '河流', '流域', '断面名称', '监测时间', '水质类别','水温', 'pH',
           '溶解氧',  '高锰酸钾', '氨氮',  '总磷','总氮'	,'电导率','浊度']
    #提取列
    data = df[columns].copy()
    data.dropna()
    # 评价城市的水质类别
    targets = '城市'
    data[targets].unique()

    #标签
    labels = ['劣Ⅴ', 'Ⅴ', 'Ⅳ', 'Ⅲ', 'Ⅱ', 'Ⅰ']

    # 水温分箱(分箱操作困难)
    # 利用机器学习 X=水温 Y=水质
    water_temperature_bins = [0,2,3,5,6,7.5,999]
    # ph分箱(分箱操作困难)
    ph_bins = [14,9,8,7.5,7,6.5,999]
    #溶解氧分箱 50是上限 不然无法分箱
    dissolved_oxygen_bins = [0,2,3,5,6,7.5,999]
    #高锰酸钾分箱
    KMnO4_bins = [0,2,4,6,10,15,999]
    #氨氮分箱
    NH4_N_bins = [0,0.15,0.5,1,1.5,2,999]

    #总磷(湖)
    P_bins = [0,0.02,0.1,0.2,0.3,0.4,50]

    #总氮
    N_bins = [0,0.2,0.5,1,1.5,2,50]

    #电导率
    conductivity_bins = []
    #浊度
    turbidity_bins = []

    #对应关系
    bins_set = {
        '水温':water_temperature_bins,
        'pH':ph_bins,
        '溶解氧':dissolved_oxygen_bins,
        '高锰酸钾':KMnO4_bins,
        '氨氮':NH4_N_bins,
        '总磷':P_bins,
        '总氮':N_bins,
        '电导率':conductivity_bins,
        '浊度':turbidity_bins,
    }
    # 进行分箱的列
    bins_columns=['溶解氧',  '高锰酸钾', '氨氮',  '总磷','总氮']

    # 进行分箱处理 使连续数值变为类别
    for i in bins_columns:
        data.loc[:,i]=pd.cut(x=data[i], bins=bins_set[i], right=False, labels=labels, retbins=False)

    # 确定评价矩阵R
    # 初始化评价矩阵R
    R_matrix = pd.DataFrame(index=bins_columns, columns=labels)

    for col in bins_columns:
        # 次数统计
        A = data[data['城市'] == '盘锦市'][col].value_counts() / len(data[data['城市'] == '盘锦市'])

        for i in labels:
            R_matrix.loc[col, i] = A.loc[i]
    #权重向量(权重相加为1) (此处为平均)
    W = np.matrix([0.2,0.2,0.2,0.2,0.2,0.2])

    #综合评价矩阵
    R = np.matrix(R_matrix.values)
    B = FuzzyEvaluation().M3(W, R)






    # R = np.matrix([[0.5,0.3,0.2,0],[0.3,0.4,0.2,0.1],[0.2,0.2,0.3,0.3]])
    # W = np.matrix([0.3,0.3,0.4])
    # ans  = FuzzyEvaluation().M4(W,R)


