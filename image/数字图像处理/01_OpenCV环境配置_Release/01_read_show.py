# Author: Shilong YANG
# Date: 2022-06-29
# Desc: Load an image and show.

import cv2 as cv
import matplotlib.pyplot as plt

IMG_DIR = '01_Resource/'
imfile = IMG_DIR + 'lena_std.tif'
im = cv.imread(imfile)
plt.subplot(1, 2, 1)
plt.imshow(im)
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
plt.subplot(1, 2, 2)
plt.imshow(im)
plt.show()
