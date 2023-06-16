#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/15 19:27
# @Author  : suxiaorui

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 16:11
# @Author  : suxiaorui

import cv2
import numpy as np

img = cv2.imread('../images/fushi.png',cv2.IMREAD_UNCHANGED)

#设置卷积核
kernel = np.ones((5,5),np.uint8)

#图像腐蚀处理
'''
res = cv2.erode(src,kernel,iterations)
src是文件，kernal是卷积核大小，iterations是迭代次数，如果不设置，一般默认为是1
'''
res = cv2.erode(img,kernel)
#如果效果不好，可以迭代多次达到好的效果
#res = cv2.erode(gray_img,kernel,iterations=5)

cv2.imshow('img',img)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()