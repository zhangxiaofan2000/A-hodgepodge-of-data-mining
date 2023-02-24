# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/19 17:27
# File : 贝叶斯.py
import numpy as np
from sklearn.decomposition import PCA

from cifar.load_cifar10 import CreatData


def preprocess_data(data, labels):
    data = data / 255.0



    return data, labels
# 获取CIFAR-10数据集
traindata, trainlabels, testdata, testlabels = CreatData()

traindata, trainlabels = preprocess_data(traindata, trainlabels)
testdata, testlabels = preprocess_data(testdata, testlabels)
# 使用PCA降维
pca = PCA(n_components=100)
X_train = pca.fit_transform(traindata)
X_test = pca.transform(testdata)

from sklearn.naive_bayes import GaussianNB
# 创建模型
model = GaussianNB()
# 训练模型
model.fit(X_train, trainlabels)
# 在测试集上进行预测
y_pred = model.predict(X_test)
# 计算准确率
accuracy = model.score(X_test, testlabels)
print("测试集准确率：{:.2f}".format(accuracy))

