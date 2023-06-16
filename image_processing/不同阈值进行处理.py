#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 20:20
# @Author  : suxiaorui



#encoding:utf-8
import cv2
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#读取图像
img=cv2.imread('../images/heidian.png')
lenna_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#阈值化处理
n, res1=cv2.threshold(gray_img,80,255,cv2.THRESH_BINARY)
n, res2=cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY)
n, res3=cv2.threshold(gray_img,150,255,cv2.THRESH_BINARY)
# n, res2=cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY_INV)
# n, res3=cv2.threshold(gray_img,160,255,cv2.THRESH_TRUNC)
# n, res4=cv2.threshold(gray_img,127,255,cv2.THRESH_TOZERO)
# n, res5=cv2.threshold(gray_img,127,255,cv2.THRESH_TOZERO_INV)

#显示结果
titles = ['原始图像','阈值T=80','阈值T=120','阈值T=150']
images = [gray_img, res1, res2, res3]
for i in range(4):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()
