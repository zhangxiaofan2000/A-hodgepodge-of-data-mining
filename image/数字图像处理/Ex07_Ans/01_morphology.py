'''
May you do good and not evil.
May you find forgiveness for yourself and forgive others.
May you share freely, never taking more than you give.
'''

# Shilong YANG

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images_09/'
imfile = IMG_DIR + 'Prob10.24.jpg'
im = cv.imread(imfile, cv.IMREAD_GRAYSCALE)
plt.subplot(2, 3, 1)
plt.imshow(im, 'gray')
plt.title('Original')

# convert to binary image
ret, im_bw = cv.threshold(im, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)	# avec la méthode Otsu
plt.subplot(2, 3, 2)
plt.imshow(im_bw, 'gray')
plt.title('Binary')

# erosion
kernel = np.ones((3, 3), dtype=np.uint8)
im_erosion = cv.erode(im_bw, kernel, 1)
plt.subplot(2, 3, 3)
plt.imshow(im_erosion, 'gray')
plt.title('eroded')

# dilation
im_dilation = cv.dilate(im_bw, kernel, 1)
plt.subplot(2, 3, 4)
plt.imshow(im_dilation, 'gray')
plt.title('Dilated')

# opening & closing operation
krnl = np.ones((3, 3), dtype=np.uint8)
im_open = cv.morphologyEx(im_bw, cv.MORPH_OPEN, krnl)
im_close = cv.morphologyEx(im_bw, cv.MORPH_CLOSE, krnl)
plt.subplot(2, 3, 5)
plt.imshow(im_open, 'gray')
plt.title('Opening')
plt.subplot(2, 3, 6)
plt.imshow(im_close, 'gray')
plt.title('Closing')

plt.show()
