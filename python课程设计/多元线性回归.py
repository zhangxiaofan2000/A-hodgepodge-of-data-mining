import numpy as np
from sklearn.linear_model import LinearRegression

# 生成两个自变量的数据
rng = np.random.RandomState(10)
x1 = rng.normal(100, 100, 50)
x2 = rng.normal(200, 200, 50)
x = np.column_stack((x1, x2))

# 生成因变量的数据
y = 10 * x1 + 5 * x2 - 10

# 拟合多元线性回归模型
model = LinearRegression(fit_intercept=True)
model.fit(x, y)

# 输出模型的系数和截距
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)

# 计算模型的判定系数
print('方程的判定系数(R^2): %.6f' % model.score(x, y))

