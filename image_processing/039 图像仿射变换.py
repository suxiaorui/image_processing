#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 9:49
# @Author  : suxiaorui

import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取图片
src = cv2.imread('lena.bmp')

#获取图像大小
rows, cols = src.shape[:2]

#设置图像仿射变换矩阵
# pos1为变换前的位置，pos2为变换后的位置
pos1 = np.float32([[50,50], [200,50], [50,200]])
pos2 = np.float32([[10,100], [200,50], [100,250]])
M = cv2.getAffineTransform(pos1, pos2)

#图像仿射变换
# src表示原图像，M表示仿射变换矩阵，(cols, rows)表示变换后的图像大小
result = cv2.warpAffine(src, M, (cols, rows))

#显示图像
cv2.imshow("original", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
