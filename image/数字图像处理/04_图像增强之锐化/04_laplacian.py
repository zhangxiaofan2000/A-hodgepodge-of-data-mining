import cv2
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images/'

# 图像锐化：拉普拉斯算子 (Laplacian)
imfile = IMG_DIR + 'moon.jpg'
img = cv2.imread(imfile, flags=0)  # NASA 月球影像图

# 使用函数 filter2D 实现 Laplace 卷积算子
kernLaplace = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])  # Laplacian kernel
imgLaplace1 = cv2.filter2D(img, -1, kernLaplace, borderType=cv2.BORDER_REFLECT)

# 使用 cv2.Laplacian 实现 Laplace 卷积算子
imgLaplace2 = cv2.Laplacian(img, -1, ksize=3)
imgRecovery = cv2.add(img, imgLaplace2)  # 恢复原图像

# 二值化边缘图再卷积
ret, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
imgLaplace3 = cv2.Laplacian(binary, cv2.CV_64F)
imgLaplace3 = cv2.convertScaleAbs(imgLaplace3)

imgs = [img, imgLaplace1, imgLaplace2, imgRecovery, imgLaplace3]
labels = ['Original NASA Moon', 'filter2D', 'cv.Laplacian', 'Recovered', 'thresh-Laplacian']
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(imgs[i], 'gray')
    plt.title(labels[i])

plt.tight_layout()
plt.show()
