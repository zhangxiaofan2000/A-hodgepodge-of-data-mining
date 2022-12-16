# Author: Shilong YANG

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = 'images/'
imfile = IMG_DIR + 'bone-scan-GE.tif'
im = cv.imread(imfile, 0)

# restore with laplacian operation.
krnl_laplace = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
im_laplace = cv.filter2D(im, -1, krnl_laplace, borderType=cv.BORDER_REFLECT)

# sobel gradient image
sobel_x = cv.Sobel(im, cv.CV_16S, 1, 0)
sobel_y = cv.Sobel(im, cv.CV_16S, 0, 1)
absX = cv.convertScaleAbs(sobel_x)
absY = cv.convertScaleAbs(sobel_y)
im_sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
im_sobel_smooth = cv.blur(im_sobel, (5, 5))

# create mask image by multiplying laplacian and smoothed sobel
im_mask = cv.multiply(im_laplace, np.uint8(im_sobel_smooth / 255))

# further enhance the image with the mask and gamma correct
im_masked = cv.add(im_mask, im)
im_ret = np.power(im_masked, 0.5)

# display original image and enhanced image for comparison
plt.subplot(121)
plt.imshow(im, 'gray')
plt.title('Original image')

plt.subplot(122)
plt.imshow(im_ret, 'gray')
plt.title('Enhanced image')
plt.show()
