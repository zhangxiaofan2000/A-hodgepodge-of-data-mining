# Author: Shilong YANG
# Desc: Display multiple images

import cv2 as cv
import matplotlib.pyplot as plt

images = ['4.2.06.tiff', '5.2.08.tiff', '7.1.09.tiff', 'boat.512.tiff']
titres = ['Boat', 'Couple', 'Tank', 'Ship']
count = 0
IMG_DIR = '01_Resource/'

for i in images:
    im = cv.imread(IMG_DIR + i)
    im = cv.cvtColor(im, cv.COLOR_BGR2RGB)	# unless specified, gray images are of 3 channels
    count += 1
    plt.subplot(2, 2, count)
    plt.imshow(im)
    plt.title(titres[count - 1])

plt.show()
