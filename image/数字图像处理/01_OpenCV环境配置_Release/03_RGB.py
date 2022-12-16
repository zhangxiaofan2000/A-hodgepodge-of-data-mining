# Please note, OpenCV is stored in B, G, R order!!!

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

IMG_DIR = '01_Resource/'
imfile = IMG_DIR + 'lena_std.tif'
im = cv.imread(imfile)
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)

# Showing Original
plt.subplot(2, 2, 1)
plt.imshow(im)
plt.title('Original')

# Extract Red Channel.
red = im.copy()
red[:,:,1] = 0
red[:,:,2] = 0
plt.subplot(2, 2, 2)
plt.imshow(red)
plt.title('Red Channel')

# Extract Green Channel
green = im.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0
plt.subplot(2, 2, 3)
plt.imshow(green)
plt.title('Green Channel')

# Extract Blue Channel
blue = im.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0
plt.subplot(2, 2, 4)
plt.imshow(blue)
plt.title('Blue Channel')

plt.show()
