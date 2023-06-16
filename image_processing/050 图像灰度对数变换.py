#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 15:44
# @Author  : suxiaorui

'''
图像灰度对数变换
DB =  c * log(1 + DA)
c为尺度比较常数，DA为原始图像灰度值，DB为变换后的目标灰度值
由于对数曲线在像素值低的区域斜率大，在像素值高的区域斜率小，所以图像经过对数变换后，较暗的区域对比度将
有所提升。可以用于增强图像的较暗的细节。

'''

import numpy as np
import matplotlib.pyplot as plt
import cv2

#绘制曲线
def log_plot(c):
    x = np.arange(0, 256, 0.01)
    y = c * np.log(1 + x)
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif']=['SimHei'] #正常显示中文标签
    plt.title(u'对数变换函数')
    plt.xlim(0, 255), plt.ylim(0, 255)
    plt.show()

#对数变换
def log(c, img):
    output = c * np.log(1.0 + img)
    output = np.uint8(output + 0.5)
    return output

#读取原始图像
img = cv2.imread('../images/street.png')

#绘制对数变换曲线
log_plot(42)

#图像灰度对数变换
output = log(42, img)

#显示图像
cv2.imshow('Input', img)
cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
