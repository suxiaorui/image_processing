#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 17:01
# @Author  : suxiaorui


import cv2
import numpy as np

image = cv2.imread('moon.png',0)
m,n = image.shape

moon = np.copy(image)
moon = moon.astype("float")

grd = np.zeros((m,n))

for x in range(m-1):
    for y in range(n-1):
        gx = abs(moon[x+1,y] - moon[x,y])
        gy = abs(moon[x,y+1] - moon[x,y])
        grd[x,y] = gx + gy

res = moon + grd
res = np.where(res< 0, 0, np.where(res > 255, 255, res))
grd = grd.astype("uint8")
res= res.astype("uint8")
cv2.imshow("image", image)
cv2.imshow("gradient", grd)
cv2.imshow("res", res)
cv2.waitKey()

