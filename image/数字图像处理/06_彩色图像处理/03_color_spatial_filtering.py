# Author: Shilong YANG
# Desc: Color image spatial filtering using Gaussian Blurring
# Date: 2022-07-17

import cv2 as cv
import matplotlib.pyplot as plt

IMG_DIR = '06_images/'
imfile = IMG_DIR + 'kodim23.png'
im = cv.imread(imfile)

# Display original image
plt.subplot(1, 2, 1)
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
plt.imshow(im)
plt.title('Original Image')

# Process and display
im_ret = cv.GaussianBlur(im, (13, 13), 3)
plt.subplot(1, 2, 2)
plt.imshow(im_ret)
plt.title('Filtered Color Image')
plt.show()
