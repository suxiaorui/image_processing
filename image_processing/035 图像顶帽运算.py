#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/15 20:18
# @Author  : suxiaorui


#encoding:utf-8
import cv2
import numpy as np

#读取图片
src = cv2.imread('../images/j.png', cv2.IMREAD_UNCHANGED)

#设置卷积核
kernel = np.ones((5,5), np.uint8)

#图像顶帽运算——原始图像减去开运算的图像，得到图像的噪声
result = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)

#显示图像
cv2.imshow("src", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
