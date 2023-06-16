#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 19:50
# @Author  : suxiaorui


import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread('lena.bmp')
lenna_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Roberts算子 常用来处理有陡峭的低噪声图像
# res = cv2.filter2D()
'''
src 表示输入原图像
res 表示输出的边缘图，其大小和通道数与输入图像相同
ddepth 表示目标图像所需的深度
kernel 表示卷核积，一个单通道浮点型矩阵
anchor 表示内核的基准点，其默认值(-1,-1)，位于中心位置
delta 表示在存储目标图像前可选的添加到像素的值，默认值为0
borderType 表示边框模式
'''
kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)
# 转uint8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 显示图形
titles = [u'原始图像', u'Roberts算子']
images = [lenna_img, Roberts]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
