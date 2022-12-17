# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/17 16:25
# File : ImageCut.py

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def watershed_demo(src):
    print(src.shape)
    # blur
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)
    # gray(binary,img)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    # open
    nb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    # close
    sure_bg = cv.dilate(nb, kernel)
    cv.imshow("morph", sure_bg)

    # distance transform
    dist = cv.distanceTransform(sure_bg, cv.DIST_L2, 3)
    cv.imshow("demo", dist)
    dist_output = cv.normalize(dist, 0, 2.0, cv.NORM_MINMAX)
    cv.imshow("distance", dist_output)

    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface", surface)

    surface_fg = np.uint8(surface)
    unkown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed
    markers = markers + 1
    markers[unkown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 255, 0]
    cv.imshow("result", src)

src = cv.imread(".\image_4\moon.jpg")
watershed_demo(src)
cv.imshow("oringnal", src)

cv.waitKey(0)
cv.destroyAllWindows()
