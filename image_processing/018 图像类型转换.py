# encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
图像类型转换
图像类型转换是将一种类型转换成另一种类型，比如彩色图像转换成灰色图像，GBR图像转换成RGB图像
"""

# 读取图片
src = cv2.imread('lena.bmp')

# 图像类型转换
result = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# result = cv2.cvtColor(src, cv2.COLOR_BGRA2RGB)
# result = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 显示图像
cv2.imshow("src", src)
cv2.imshow("result", result)


# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
