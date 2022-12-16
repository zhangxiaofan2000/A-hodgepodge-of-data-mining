# Author: Shilong YANG
# Desc: Image addition and subtraction using OpenCV
# Date: 2022-07-22

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = '01_images/'

imfile = IMG_DIR  + 'Baboon.bmp'
imfile2 = IMG_DIR  + 'lena.bmp'
imfile3 = IMG_DIR  + 'elaine.512.tiff'
noir_coeur = IMG_DIR + 'noir_coeur.bmp'
baboon = cv.imread(imfile)
lena = cv.imread(imfile2)
elaine = cv.imread(imfile3)
mask = cv.imread(noir_coeur)


# displaying original images on line 1
plt.subplot(2, 3, 1)
plt.imshow(baboon, 'gray')
plt.title('Baboon')
plt.subplot(2, 3, 2)
plt.imshow(lena, 'gray')
plt.title('Lenna')
plt.subplot(2, 3, 3)
plt.imshow(elaine, 'gray')
plt.title('Elaine')

# image addition
ret = cv.add(baboon, lena)
plt.subplot(2, 3, 4)
plt.imshow(ret, 'gray')
plt.title('Image Addition')

# image subtraction
ret = cv.subtract(elaine, lena)
plt.subplot(2, 3, 5)
plt.imshow(ret, 'gray')
plt.title('Image Subtraction')

# image multiply: You should normalize the mask before multiplication.
ret = cv.multiply(elaine, np.uint8(mask / 255))
plt.subplot(2, 3, 6)
plt.imshow(ret, 'gray')
plt.title('Image Multiply')
plt.show()
