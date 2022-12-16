# Author: Shilong YANG
# Desc: Randomized image
# Date: 2022-07-15

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random as rd

# define our dimennsion to be 512
dimen = 512
pic = np.zeros((dimen, dimen), dtype=np.uint8)

for i in range(dimen):
	for j in range(dimen):
		pic[i][j] = rd.randrange(0, 256)
		
plt.imshow(pic, 'gray')
plt.title('Random image')
plt.show()
