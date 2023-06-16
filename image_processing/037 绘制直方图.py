#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/15 20:24
# @Author  : suxiaorui


#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('1.bmp')
cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyAllWindows()

# hist可以绘制直方图，前提需要的是一维数组，ravel函数能将数组降成一维数组
plt.hist(src.ravel(), 256)
plt.show()
