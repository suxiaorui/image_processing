# encoding:utf-8
import cv2
import numpy as np

"""
图像缩放三种方式

"""

# 读取图片
src = cv2.imread('lena.bmp')
rows,cols = src.shape[:2]

# 图像缩放
res1 = cv2.resize(src, (200, 100))
res2 = cv2.resize(src,(int(cols*0.6),int(rows*1.2)))
res3 = cv2.resize(src,None,fx=0.5,fy=0.5)

# 显示图像
cv2.imshow("src", src)
cv2.imshow("res1", res1)
cv2.imshow("res2", res2)
cv2.imshow("res3", res3)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
