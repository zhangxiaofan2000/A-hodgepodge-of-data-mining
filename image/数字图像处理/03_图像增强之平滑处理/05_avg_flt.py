# Author: Shilong YANG
# Desc: average filtering
# Date: 20220715

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images/'
imfile = IMG_DIR + 'salt_pepper.bmp'
im = cv.imread(imfile)

img_3 = cv.blur(im, (3, 3))
img_7 = cv.blur(im, (7, 7))

plt.subplot(1, 2, 1)
plt.imshow(img_3)
plt.title('Average Filter ($3\\times3$)')

plt.subplot(1, 2, 2)
plt.imshow(img_7)
plt.title('Average Filter ($7\\times7$)')

plt.show()
