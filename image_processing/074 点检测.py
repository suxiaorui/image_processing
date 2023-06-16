#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 15:52
# @Author  : suxiaorui


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('lena_.bmp')

kernel = np.array((
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]), dtype="float32")

res = cv2.filter2D(img,-1,kernel)


#显示图像
title = ['Source Image','Res Image']
images = [img,res]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(title[i])
plt.show()

