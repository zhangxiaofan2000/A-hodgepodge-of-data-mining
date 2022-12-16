import cv2 as cv
import matplotlib.pyplot as plt
import os

result_holder = './Result/'
if not os.path.exists(result_holder):
	os.makedirs(result_holder)

# read and display original image
IMG_DIR = '01_images/'

imfile = IMG_DIR + 'F16.bmp'
im = cv.imread(imfile)
plt.subplot(2, 3, 1)
plt.imshow(im)
plt.title('Original image')

# nearest interpolation
im_nearest = cv.resize(im, (512, 512), interpolation=cv.INTER_NEAREST)
cv.imwrite('Result/zoomin_nearest.bmp', im_nearest)

# bilinear interpolate
im_bilinear= cv.resize(im, (512, 512), interpolation=cv.INTER_LINEAR)
cv.imwrite('Result/zoomin_bilinear.bmp', im_bilinear)

# cubic interpolation
im_cubic = cv.resize(im, (512, 512), interpolation=cv.INTER_CUBIC)
cv.imwrite('Result/zoomin_cubic.bmp', im_cubic)

# draw them all
plt.subplot(2, 3, 2)
plt.imshow(im_nearest)
plt.title('Nearest Interpolate')

plt.subplot(2, 3, 3)
plt.imshow(im_bilinear)
plt.title('Bilinear Interpolation')

plt.subplot(2, 3, 4)
plt.imshow(im_cubic)
plt.title('Cubic Interpolation')

plt.show()
