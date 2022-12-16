# Image clipping and rotation
# AUthor: Shilong YANG
# Date: 20220713

import cv2 as cv
import matplotlib.pyplot as plt

IMG_DIR = '01_images/'

imfile = IMG_DIR + 'want_want.jpg'
im = cv.imread(imfile)
plt.subplot(1, 3, 1)
plt.imshow(im)
plt.title('Original Image')
(height, width, c) = im.shape

# we rotate by 45 degrees clockwise and therefore -45
aff_mat = cv.getRotationMatrix2D((height/2, width/2), -45, 1)
dst = cv.warpAffine(im, aff_mat, (width, height))
plt.subplot(1,3,2)
plt.imshow(dst)
plt.title('Rotate by 45 degs')

# clipping image
cropped = im[25:205, 196:283]
plt.subplot(1,3,3)
plt.imshow(cropped)
plt.title('Cropped')
plt.show()
