import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images/'

imfile = IMG_DIR + 'house.jpg'
im = cv.imread(imfile, cv.IMREAD_GRAYSCALE)
title_list = ['Original Image', 'Canny', 'Roberts', 'Sobel']

# canny operator
canny = cv.Canny(im, 50, 150)

krnl_x = np.array([[-1, 0], [0, 1]], dtype=int) 
krnl_y = np.array([[0, -1], [1, 0]], dtype=int)
x = cv.filter2D(im, cv.CV_16S, krnl_x) 
y = cv.filter2D(im, cv.CV_16S, krnl_y)
absX = cv.convertScaleAbs(x) 
absY = cv.convertScaleAbs(y) 
roberts = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# Sobel operator
x = cv.Sobel(im, cv.CV_16S, 1, 0)
y = cv.Sobel(im, cv.CV_16S, 0, 1)
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

image_list = [im, canny, roberts, sobel]

for i in range(4):
	plt.subplot(2, 2, i + 1)
	plt.imshow(image_list[i], 'gray')
	plt.title(title_list[i])

plt.show()
