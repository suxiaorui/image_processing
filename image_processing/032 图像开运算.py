#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/15 20:04
# @Author  : suxiaorui
#encoding:utf-8

import cv2
import numpy as np

#读取图片
src = cv2.imread('../images/i.png', cv2.IMREAD_UNCHANGED)

#设置卷积核
kernel = np.ones((5,5), np.uint8)
#这样处理发现还有噪声，就将卷积核变成(10,10)

#图像开运算
result = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)

#显示图像
cv2.imshow("src", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
