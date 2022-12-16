# Author: Shilong YANG
# Desc: Generate negative images

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images/'
imfile = IMG_DIR + 'rock.jpg'
im = cv.imread(imfile)

plt.subplot(1, 2, 1)
plt.imshow(im)
plt.title('Original image')

img = cv.normalize(im, None, alpha=0, beta=500, norm_type=cv.NORM_MINMAX)
plt.subplot(1, 2, 2)
plt.imshow(img, 'gray')
plt.title('Gray scale stretched')

plt.show()
