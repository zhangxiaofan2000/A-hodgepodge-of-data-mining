import numpy as np


class KMeans:
    def __init__(self, n_clusters, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.iter_plot = list()
    def fit(self, X):
        n_samples, n_features = X.shape

        # 随机初始化聚类中心
        self.centers = np.random.rand(self.n_clusters, n_features)

        for i in range(self.max_iter):
            # 计算每个样本到每个聚类中心的距离
            distances = np.sqrt(((X - self.centers[:, np.newaxis]) ** 2).sum(axis=2))
            # 将每个样本分配到最近的聚类中心
            self.labels = np.argmin(distances, axis=0)
            # 计算新的聚类中心
            for j in range(self.n_clusters):
                self.centers[j] = X[self.labels == j].mean(axis=0)

            # 如果迭代次数超过10次，则计算质心距离和差异准则的值
            if i > 10:
                inertia = self.calc_inertia(X, self.labels)
                self.iter_plot.append(inertia)
                print("迭代次数 {}: 质心距离 = {}".format(i, inertia))

    def predict(self, X):
        n_samples, _ = X.shape
        # 计算每个样本到每个聚类中心的距离
        distances = np.sqrt(((X - self.centers[:, np.newaxis]) ** 2).sum(axis=2))
        # 将每个样本分配到最近的聚类中心
        return np.argmin(distances, axis=0)
    def calc_inertia(self,X, labels):
        """计算质心距离和差异准则的值"""
        distances = 0
        for i in range(self.n_clusters):
            # 计算每个样本到聚类中心的距离
            center = self.centers[i]
            samples = X[labels == i]
            d = ((samples - center) ** 2).sum(axis=1)
            distances += d.sum()
        return distances
