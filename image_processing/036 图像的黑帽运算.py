#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/15 20:21
# @Author  : suxiaorui

#encoding:utf-8
import cv2
import numpy as np

#读取图片
src = cv2.imread('../images/jj.png', cv2.IMREAD_UNCHANGED)

#设置卷积核
kernel = np.ones((5,5), np.uint8)

#图像黑帽运算——指闭运算减去原始图像得到的图像内部的小孔或者小点。
result = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)

#显示图像
cv2.imshow("src", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
