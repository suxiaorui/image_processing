#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 20:50
# @Author  : suxiaorui


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.bmp')
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 图像平移 下、上、右、左平移
'''
图像平移首先得定义平移矩阵，然后再调用warpAffine函数实现平移
M = np.float32([[1, 0, x], [0, 1, y]])    
res = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
'''
M = np.float32([[1, 0, 0], [0, 1, 100]])
img1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

M = np.float32([[1, 0, 0], [0, 1, -100]])
img2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

M = np.float32([[1, 0, 100], [0, 1, 0]])
img3 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

M = np.float32([[1, 0, -100], [0, 1, 0]])
img4 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

titles = ['Image1', 'Image2', 'Image3', 'Image4']
images = [img1, img2, img3, img4]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
