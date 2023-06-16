#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 16:12
# @Author  : suxiaorui

#encoding:utf-8
import cv2
import matplotlib.pyplot as plt

#读取图像
img=cv2.imread('lena.bmp')
lenna_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#阈值化处理
n, res1=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
n, res2=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY_INV)
n, res3=cv2.threshold(gray_img,127,255,cv2.THRESH_TRUNC)
n, res4=cv2.threshold(gray_img,127,255,cv2.THRESH_TOZERO)
n, res5=cv2.threshold(gray_img,127,255,cv2.THRESH_TOZERO_INV)

#显示结果
titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [gray_img, res1, res2, res3, res4, res5]
for i in range(6):
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()
