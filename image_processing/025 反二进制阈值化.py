#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 15:57
# @Author  : suxiaorui

import cv2

img = cv2.imread('lena.bmp')

# 灰度图像处理
gray_img = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)

#二进制阈值化处理，这里将大于127设置为0，小于的话设置为255
#返回n和res，n为127，res为处理后的结果
n, res = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY_INV)


cv2.imshow('img',img)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()