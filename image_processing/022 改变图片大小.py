#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 18:53
# @Author  : suxiaorui
# @File    : 022 改变图片大小.py

import cv2
import glob

i = 0
all_path = glob.glob('../CT_COVID/*.png')
for path in all_path:
    images = cv2.imread(path)
    res = cv2.resize(images, (64, 64))
    cv2.imwrite('D:\work\small_images{}.jpg'.format(i),res)
    i = i + 1






