# Author: Shilong YANG
# Desc: Generate negative images

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images/'
imfile = IMG_DIR + 'Fig3.09(a).jpg'
im = cv.imread(imfile)

plt.subplot(1, 2, 1)
plt.imshow(im)
plt.title('Original image')

im_norm = im / 255
gamma = 5
dst = np.power(im_norm, gamma)
plt.subplot(1, 2, 2)
plt.imshow(dst, 'gray')
plt.title('Gamma corrected ($\gamma = 5.0$)')
plt.show()
