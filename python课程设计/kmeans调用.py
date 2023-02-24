import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from python课程设计.KMeans import KMeans

X  = np.array(pd.read_csv("./testSet.csv",header=None).values.tolist())

#可视化X
plt.figure(figsize=(12, 9))
plt.plot(X,  'o')
plt.show()
# 创建 KMeans 对象，并调用 fit 方法拟合聚类模型
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# 调用 predict 方法预测每个样本的类别
y_pred = kmeans.predict(X)

# 可视化聚类结果
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()


# 可视化质心距离迭代过程
plt.plot(kmeans.iter_plot)
plt.show()