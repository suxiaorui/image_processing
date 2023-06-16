#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 20:03
# @Author  : suxiaorui


import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread('lena.bmp')
lenna_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel算子 常用于噪声较多、灰度渐变的图像
'''
res = Sobel()
src 表示输入原图像
res 表示输出的边缘图，其大小和通道数与输入图像相同
ddepth 表示目标图像所需的深度
dx 表示x方向上的差分阶数，取值为1或者0
dy 表示y方向上的差分阶数，取值为1或者0
ksize 表示Sobel算子的大小，其值必须是正数和奇数
scale 表示缩放导数的比列常数，默认情况下没有伸缩系数
delta 表示在存储目标图像前可选的添加到像素的值，默认值为0
borderType 表示边框模式
'''
x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)  # 对x求一阶导
y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)  # 对y求一阶导
'''
res = convertScaleAbs() 用来计算绝对值，并将图像转换为8位图进行显示
src 表示原数组
det 表示输出数组，深度为8位
alpha 表示比例因子
beta 表示原数组按比例缩放后添加的值
'''
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 显示图形
titles = [u'原始图像', u'Sobel算子']
images = [lenna_img, Sobel]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
