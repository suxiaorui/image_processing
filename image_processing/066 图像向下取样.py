#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/19 16:18
# @Author  : suxiaorui



import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('lena.bmp')

#图像向下取样
r = cv2.pyrDown(img)

#显示图像
cv2.imshow('original', img)
cv2.imshow('PyrDown', r)
cv2.waitKey()
cv2.destroyAllWindows()
