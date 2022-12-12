import matplotlib.pyplot as plt

# 计算欧拉螺线上的点的坐标
x = []
y = []

a, b = 137.508, 200
n = 1000

for i in range(n):
  x.append(x[-1] + 1)
  y.append(y[-1] + a / b)

# 画欧拉螺线
plt.plot(x, y)

# 显示图形
plt.show()
