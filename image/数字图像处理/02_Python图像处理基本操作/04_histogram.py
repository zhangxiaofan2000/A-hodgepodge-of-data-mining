# Author: Shilong YANG
# Desc: Histogram calculate and equalization

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# prepare file name and load image
IMG_DIR = '01_images/'
imfile = IMG_DIR + 'boat.512.tiff'
im = cv.imread(imfile, cv.IMREAD_GRAYSCALE)

# define a function to show histogram
def imhist(im, i, titre):
	hist = cv.calcHist([im], [0], None, [256], [0, 256])
	plt.subplot(2, 2, i)
	plt.hist(im.ravel(), 256, [0, 256]);
	plt.title(titre)
	
# showing original image and its histogram
plt.subplot(2, 2, 1)
plt.imshow(im, 'gray')
plt.title('Original image')
imhist(im, 2, 'Original histogram')

# perform histogram equalization
im_eq = cv.equalizeHist(im)
plt.subplot(2, 2, 3)
plt.imshow(im_eq, 'gray')
plt.title('Equalized image')
imhist(im_eq, 4, 'Equalized histogram')
plt.show()
