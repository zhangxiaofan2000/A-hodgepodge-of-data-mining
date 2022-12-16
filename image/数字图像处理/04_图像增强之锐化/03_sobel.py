# Author: Shilong YANG
# Calculating Sobel Result with Filter2D

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = './images/'
imfile = IMG_DIR + 'house.jpg'

im = cv.imread(imfile, cv.IMREAD_GRAYSCALE)
krnl_x = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], int)
krnl_y = krnl_x.transpose()

sobel_x = cv.filter2D(im, cv.CV_16S, krnl_x)
sobel_y = cv.filter2D(im, cv.CV_16S, krnl_y)

# compute absolute value of each operation result
absX = cv.convertScaleAbs(sobel_x)
absY = cv.convertScaleAbs(sobel_y)
sobel_ret = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# disply our result
imgs = [im, absX, absY, sobel_ret]
labels = ['Original image', 'Sobel: X', 'Sobel: Y', 'Sobel']
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(imgs[i], 'gray')
    plt.title(labels[i]) 

plt.show()
