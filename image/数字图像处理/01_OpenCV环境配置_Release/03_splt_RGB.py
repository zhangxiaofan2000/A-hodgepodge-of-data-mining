# extract three channels i.e. RGB

import cv2 as cv

imfile = './01_Resource/lena_std.tif'
im = cv.imread(imfile)
im_b = im[:, :, 0]
im_g = im[:, :, 1]
im_r = im[:, :, 2]
cv.imwrite('Result/b.bmp', im_b)
cv.imwrite('Result/g.bmp', im_g)
cv.imwrite('Result/r.bmp', im_r)
