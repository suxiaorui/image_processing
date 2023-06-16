# encoding:utf-8
import cv2
import numpy as np

"""
"""

# 读取图片
src = cv2.imread('../images/lena.bmp')
#原图的高 宽 通道数
rows,cols,channel = src.shape

# 图像选转
M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
res = cv2.warpAffine(src,M,(cols,rows))

# 显示图像
cv2.imshow("src", src)
cv2.imshow("res",res)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
