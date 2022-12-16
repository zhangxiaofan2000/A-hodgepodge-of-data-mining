# Author: Shilong YANG
# Desc: median filtering
# Date: 2022-07-15

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images/'
imfile = IMG_DIR + 'salt_pepper.bmp'
im = cv.imread(imfile)

img_3 = cv.medianBlur(im, 3)
img_5 = cv.medianBlur(im, 5)

plt.subplot(1, 2, 1)
plt.imshow(img_3)
plt.title('Median Filter ($3\\times3$)')

plt.subplot(1, 2, 2)
plt.imshow(img_5)
plt.title('Median Filter ($5\\times5$)')

plt.show()
