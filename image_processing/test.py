#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 19:24
# @Author  : suxiaorui

import cv2
img = cv2.imread('../CT_COVID/2020.01.24.919183-p27-132.png')

cv2.imshow('covid',img)

res = img[0:175, 0:250]
cv2.imshow('covid',res)

cv2.waitKey(0)
cv2.destroyAllWindows()