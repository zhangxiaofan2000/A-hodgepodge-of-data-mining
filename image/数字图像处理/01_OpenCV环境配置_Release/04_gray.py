import cv2 as cv
import matplotlib.pyplot as plt

IMG_DIR = '01_Resource/'

imfile = IMG_DIR + 'kodim15.png'
im = cv.imread(imfile)
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)

# Display original
plt.subplot(2, 2, 1)
plt.imshow(im)
plt.title('Original Image')

# Display V channel in hsv color space
img = 0.299 * im[:, :, 0] + 0.587 * im[:, :, 1] + 0.114 * im[:, :, 2]
plt.subplot(2, 2, 2)
plt.imshow(img, 'gray')
plt.title('HSV Method')

# Minimum
img_min = cv.min(im[:,:,0], im[:, :, 1])
img_min = cv.min(img_min, im[:, :, 2])
plt.subplot(2, 2, 3)
plt.imshow(img_min, 'gray')
plt.title('Minimum')

# Maximum
max_gray = cv.max(im[:,:,0], im[:, :, 1])
max_gray = cv.max(max_gray, im[:, :, 2])
plt.subplot(2, 2, 4)
plt.imshow(max_gray, 'gray')
plt.title('Maximum')

plt.show()
