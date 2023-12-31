#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/19 16:20
# @Author  : suxiaorui



import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('lena.bmp')

#图像向上取样
r1 = cv2.pyrUp(img)
r2 = cv2.pyrUp(r1)
r3 = cv2.pyrUp(r2)

#显示图像
cv2.imshow('original', img)
cv2.imshow('PyrUp1', r1)
cv2.imshow('PyrUp2', r2)
cv2.imshow('PyrUp3', r3)
cv2.waitKey()
cv2.destroyAllWindows()
