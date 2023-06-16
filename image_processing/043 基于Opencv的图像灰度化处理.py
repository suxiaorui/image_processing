#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 10:04
# @Author  : suxiaorui

#encoding:utf-8
import cv2
import numpy as np

#读取原始图片
src = cv2.imread('lena.bmp')

#图像灰度化处理
grayImage = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#显示图像
cv2.imshow("src", src)
cv2.imshow("result", grayImage)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
