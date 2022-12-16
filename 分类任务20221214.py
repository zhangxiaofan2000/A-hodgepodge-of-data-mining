# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/14 22:58
# File : 分类任务20221214.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import metrics

def Confusion_matrix(y_test,y_pred):
    '''
    用于绘制 混淆矩阵
    :param model: 模型
    :param X_test:
    :param y_test:
    :return:
    '''
    cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
    labels = [0, 1]
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot()
    plt.show()

def AUC(y_test,y_pred):
    '''
    用于绘制 AUC曲线
    :param y_test:
    :param y_pred:
    :return:
    '''
    fpr, tpr, threshold = metrics.roc_curve(y_test, y_pred)
    roc_auc = metrics.auc(fpr, tpr)
    plt.figure(figsize=(6, 6))
    plt.title('Validation ROC')
    plt.plot(fpr, tpr, 'b', label='Val AUC = %0.3f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()

#程序入口
if __name__ == '__main__':

    '''
    数据读取
    '''
    data = pd.read_csv("http://aisys.ai-learning.net/upfields/AiFile/1578248996309700610/drillSet.csv",header=0)
    # print(data)#读取案例数据

    '''
    数据预处理
    '''
    #缺失值处理
    data.isna().sum(axis=1) #判断是否缺失，然后按行加和，得到每列有多少缺失值
    data = data.drop("pdays",axis=1) #删除pdays,因为缺失率超过96%
    data = data.dropna()

    data1_x = data.drop(["job","marital", "education", "default", "housing", "loan", "y"],axis=1) #data1_x是所有无缺失的自变量
    data1_y = data["loan"]#让存在缺失值的loan，作为因变量，建立回归模型，从而对缺失值进行预测
    data1_y = data1_y.replace({"yes":1,"no":0})#对yes和no进行替换，变成1和0


    '''
    数据预处理
    '''
    # data1_x.columns
    data1_x['contact'] = data1_x['contact'].replace({"telephone":1,"cellular":2})
    data1_x['month'] = data1_x['month'].replace({"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,'jul':7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12})
    data1_x['day_of_week'] = data1_x['day_of_week'].replace({"mon":1,"tue":2,"wed":3,"thu":4,"fri":5})
    data1_x['poutcome'] = data1_x['poutcome'].replace({"nonexistent":0,"failure":1,"success":2})



    #
    # data1_x_train = data1_x.loc[~data1_y.isna(),:]
    # data1_x_test = data1_x.loc[data1_y.isna(),:]
    # data1_Y_train = data1_y.loc[data1_x_train.index]
    # data1_y_test = data1_y.loc[data1_x_test.index] #划分训练集和测试集，训练集是loan没有缺失的行，测试集是loan有缺失的行


    # 划分训练集和测试集 有专门的库
    from sklearn.model_selection import train_test_split

    # assume X is a matrix of feature data and y is a vector of target values
    X_train, X_test, Y_train, y_test = train_test_split(data1_x, data1_y, test_size=0.25)


    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression() #建立逻辑斯蒂回归模型
    model.fit(X_train, Y_train) #使用训练集
    y_pred = model.predict(X_test)
    Confusion_matrix(y_test,y_pred)
    AUC(y_test,y_pred)



    from sklearn.svm import SVC
    model = SVC() #建立逻辑斯蒂回归模型
    model.fit(X_train, Y_train) #使用训练集
    y_pred = model.predict(X_test)
    Confusion_matrix(y_test,y_pred)
    AUC(y_test,y_pred)



    # 梯度提升决策分类Gradient Boosting Classifier
    from sklearn.ensemble import GradientBoostingClassifier

    model = GradientBoostingClassifier()
    model.fit(X_train, Y_train) #使用训练集
    y_pred = model.predict(X_test)

    Confusion_matrix(y_test,y_pred)
    AUC(y_test,y_pred)
