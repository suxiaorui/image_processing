#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 9:51
# @Author  : suxiaorui

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
图像透视变换的本质是将图像投影到一个新的视平面，同样先构造矩阵，然后进行透视变换。
'''
#读取图片
src = cv2.imread('lena.bmp')

#获取图像大小
rows, cols = src.shape[:2]

#设置图像透视变换矩阵
pos1 = np.float32([[114, 82], [287, 156], [8, 322], [216, 333]])
pos2 = np.float32([[0, 0], [188, 0], [0, 262], [188, 262]])
M = cv2.getPerspectiveTransform(pos1, pos2)

#图像透视变换
result = cv2.warpPerspective(src, M, (190, 272))

#显示图像
cv2.imshow("original", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
