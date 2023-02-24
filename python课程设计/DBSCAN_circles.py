import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import datasets
from sklearn.cluster import DBSCAN

#%% 生成、展示数据
X1, y1=datasets.make_circles(n_samples=1000, factor=0.6,noise=0.05,random_state=9)  #factor:外圈与内圈的尺度因子
X2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2,1.2]],
                             cluster_std=[[0.1]], random_state=9)
X = np.concatenate((X1, X2))  #纵向拼接
plt.figure(figsize=(12, 9))
plt.plot(X[:, 0], X[:, 1],  'o',markersize=6)
plt.show()

#%% 首先看看K-Means的聚类效果
from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=3, random_state=9).fit_predict(X)
plt.figure(figsize=(12, 9))
plt.scatter(X[:, 0], X[:, 1],s=25, c=y_pred)
plt.title('k-means:k=3')
plt.show()
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, y_pred))

#%% 那么如果使用DBSCAN效果如何呢？我们先不调参，直接用默认参数，看看聚类效果,：
db = DBSCAN().fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)   
          for each in np.linspace(0, 1, len(unique_labels))]
#   1)np.linspace 返回[0,1]之间的len(unique_labels) 个数
#   2)plt.cm 一个颜色映射模块
#   3)生成的每个colors包含4个值，分别是RGBA:
#    RGBA是代表Red（红色） Green（绿色） Blue（蓝色）和 Alpha的色彩空间，
#    也就是透明度/不透明度
#   4)其实这行代码的意思就是生成len(unique_labels)个可以和光谱对应的颜色值
plt.figure(figsize=(12, 9))
for k, col in zip(unique_labels, colors):
    class_member_mask = (labels == k)
    if k == -1:   #被判定的噪声点
        cls =  'noise'
        xy = X[class_member_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor='k',
             markeredgecolor='k', markersize=6,label=cls)
    else:
        xy = X[class_member_mask & core_samples_mask]   #核心点
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=10,label= 'class '+ str(k)+' core')
        xy = X[class_member_mask & ~core_samples_mask]  #边缘点
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6,label= 'class '+ str(k)+' border')
plt.legend(loc='best')
plt.title('Estimated number of clusters: %d' % n_clusters_)

plt.show()

#%% 对DBSCAN的两个关键的参数eps和min_samples进行调参！发现，类别数太少，
#需要增加类别数，可以减少eps-邻域的大小，默认是0.5，减到0.1看看效果
db = DBSCAN(eps=0.1).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)   
          for each in np.linspace(0, 1, len(unique_labels))]
plt.figure(figsize=(12, 9))
for k, col in zip(unique_labels, colors):
    class_member_mask = (labels == k)
    if k == -1:   #被判定的噪声点
        cls =  'noise'
        xy = X[class_member_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor='k',
             markeredgecolor='k', markersize=6,label=cls)
    else:
        xy = X[class_member_mask & core_samples_mask]   #核心点
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=12,label='class '+ str(k)+' core')
        xy = X[class_member_mask & ~core_samples_mask]  #边缘点
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6,label='class '+ str(k)+' border')
plt.legend(loc='best')
plt.title('Estimated number of clusters: %d' % n_clusters_)

plt.show()