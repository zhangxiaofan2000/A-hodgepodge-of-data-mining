# Author: Shilong YANG
# Desc: False color enhancement
# Date: 2022-07-17

import cv2 as cv
import matplotlib.pyplot as plt

IMG_DIR = '06_images/'
imfile = IMG_DIR + 'rose.tif'
im_gray = cv.imread(imfile, cv.IMREAD_GRAYSCALE)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(im_gray, 'gray')
plt.title('Original Image')

# Process and display
im_clr = cv.applyColorMap(im_gray, cv.COLORMAP_HOT)
im_clr = cv.cvtColor(im_clr, cv.COLOR_BGR2RGB)
plt.subplot(1, 2, 2)
plt.imshow(im_clr)
plt.title('Pseudo Color Image')
plt.show()
