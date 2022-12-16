# Author: Shilong YANG
# Desc: This script add salt & pepper noise to source image
# Date: 20220715

import cv2 as cv
import random
import matplotlib.pyplot as plt

IMG_DIR = 'images/'
imfile = IMG_DIR + 'lena_std.tif'
noise_ratio = 0.05
im = cv.imread(imfile)
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(im)
plt.title('Original Image')

# read size and calculate pixel count
w, h, c = im.shape
pxl_num = w * h
noise_count = int(pxl_num * noise_ratio)

# generate noise
for i in range(noise_count):
    p_x = random.randrange(0, w)
    p_y = random.randrange(0, h)
    noise_color = random.randint(0, 1)
    if (noise_color != 0):
        im[p_x, p_y, 0] = 255
        im[p_x, p_y, 1] = 255
        im[p_x, p_y, 2] = 255
    else:
        im[p_x, p_y, 0] = 0
        im[p_x, p_y, 1] = 0
        im[p_x, p_y, 2] = 0
plt.subplot(1, 2, 2)
plt.imshow(im)
plt.title('Salt & Pepper Noise')
plt.show()

