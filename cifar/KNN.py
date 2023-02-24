# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/19 17:08
# File : KNN.py
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from cifar.load_cifar10 import CreatData

# 加载 CIFAR-10 数据集
X_train, y_train, X_test, y_test = CreatData()

# 缩放特征
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 训练 KNN 分类器
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 评估模型在测试集上的性能
accuracy = knn.score(X_test, y_test)
print("测试集准确率：{:.2f}".format(accuracy))

