# Author: Shilong YANG
# Desc: Randomized image
# Date: 2022-07-15

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random as rd

# define our dimennsion to be 512
dimen = 512

r = np.zeros((dimen, dimen), dtype=np.uint8)
g = r.copy()
b = r.copy()

for i in range(dimen):
	for j in range(dimen):
		r[i][j] = rd.randrange(0, 256)
		g[i][j] = rd.randrange(0, 256)
		b[i][j] = rd.randrange(0, 256)
		
rand_image = cv.merge([r, g, b])
plt.imshow(rand_image)
plt.title('Random image')
plt.show()
