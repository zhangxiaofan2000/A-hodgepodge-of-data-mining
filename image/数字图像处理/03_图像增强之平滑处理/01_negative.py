# Author: Shilong YANG
# Desc: Generate negative images

import cv2 as cv
import matplotlib.pyplot as plt

IMG_DIR = 'images/'
imfile = IMG_DIR + 'rose.tif'
im = cv.imread(imfile)

plt.subplot(1, 2, 1)
plt.imshow(im)
plt.title('Original image')

im_n = cv.bitwise_not(im)
plt.subplot(1, 2, 2)
plt.imshow(im_n)
plt.title('Negative image')
plt.show()
