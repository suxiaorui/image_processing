#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 17:18
# @Author  : suxiaorui

import cv2
import numpy as np

image = cv2.imread('moon.png',0)
m,n = image.shape

moon = np.copy(image)
moon = moon.astype("float")

our_def = np.zeros((m,n))
for x in range(1,m-1):
    for y in range(1,n-1):
        gx = abs((moon[x + 1, y - 1] + moon[x + 1, y] + moon[x + 1, y + 1]) - (
                moon[x - 1, y - 1] + moon[x - 1, y] + moon[x - 1, y + 1]))
        gy = abs((moon[x - 1, y + 1] + moon[x, y + 1] + moon[x + 1, y + 1]) - (
            moon[x - 1, y - 1] + moon[x, y - 1] + moon[x + 1, y - 1]))

        our_def[x,y] = gx + gy


res = moon + our_def
res = np.where(res < 0, 0, np.where(res > 255,255,res))
res = res.astype("uint8")

cv2.imshow("moon", image)
cv2.imshow("defined_res", res)
cv2.waitKey()

