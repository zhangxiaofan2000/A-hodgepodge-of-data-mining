# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/19 15:55
# File : kmeans.py
import numpy as np
from sklearn.decomposition import PCA

from cifar.load_cifar10 import CreatData

# 获取CIFAR-10数据集
traindata, trainlabels, testdata, testlabels = CreatData()

# 使用PCA降维
pca = PCA(n_components=2)
X_train = pca.fit_transform(traindata)
X_test = pca.transform(testdata)



from sklearn.cluster import KMeans

# 定义KMeans模型，并指定要分成的聚类数量
kmeans = KMeans(n_clusters=10)
# 将数据聚类到指定的聚类中
y_pred = kmeans.fit_predict(X_train)

# 使用每个聚类的众数类别作为该聚类的预测类别
pred_labels = []
for i in range(10):
    # 获取聚类i的所有数据的类别
    labels = trainlabels[y_pred == i]
    # 使用聚类i的众数类别作为该聚类的预测类别
    pred_label = np.argmax(np.bincount(labels))
    pred_labels.append(pred_label)
pred_labels = np.array(pred_labels)


# 对于每个测试样本，将其分配给那个聚类中众数类别最接近该样本的类别
predictions = []
for i in range(len(X_test)):
    # 计算测试样本i与每个聚类的中心的距离
    distances = np.linalg.norm(X_test[i] - kmeans.cluster_centers_, axis=1)
    # 将测试样本i分配到距离最小的聚类中
    cluster = np.argmin(distances)
    # 获取聚类中的众数类别作为测试样本i的预测类别
    prediction = pred_labels[cluster]
    predictions.append(prediction)
predictions = np.array(predictions)

from sklearn.metrics import accuracy_score

# 计算准确率
accuracy = accuracy_score(testlabels, predictions)
print('准确率:', accuracy)


import matplotlib.pyplot as plt


# 使用不同的颜色区分不同的聚类
colors = ['orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'teal', 'maroon', 'navy']


# 绘制测试样本的分布情况
for i in range(len(X_test)):
    x = X_test[i][0]
    y = X_test[i][1]
    color = colors[predictions[i]]
    plt.scatter(x, y, c=color)

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red')

plt.show()
