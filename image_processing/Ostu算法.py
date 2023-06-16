#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 18:39
# @Author  : suxiaorui


import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
np.seterr(divide='ignore',invalid='ignore')

#计算图像灰度直方图
def calc_grayhist(image):
    rows,cols = image.shape
    #存储灰度直方图
    grayhist = np.zeros([1,256],np.uint32)
    for i in range(rows):
        for j in range(cols):
            grayhist[0][image[i][j]] += 1
    return grayhist

def ostu(image):
    rows,cols = image.shape
    mean_weigth = 1.0 / (rows * cols)
    his, bins = np.histogram(image, np.arange(0, 257))
    final_thresh = -1
    final_value = -1
    intensity_arr = np.arange(256)
    for t in bins[1:-1]:
        pcb = np.sum(his[:t])
        pcf = np.sum(his[t:])
        Wb = pcb * mean_weigth
        Wf = pcf * mean_weigth
        mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
        muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)
        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    print(final_value)
    print(final_thresh)
    final_img = image.copy()
    final_img[image > final_thresh] = 255
    final_img[image < final_thresh] = 0
    return final_img



image = cv2.imread('id.png',cv2.IMREAD_COLOR)
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('image1',image)
cv2.imshow('res',ostu(image))

plt.hist(image.ravel(), 256)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()