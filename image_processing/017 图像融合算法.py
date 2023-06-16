
import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
图像融合
用cv2.addWeighted(src1,alpha,src2,beta,gamma)
图像融合：目标图像 = 图像1 * 系数1 + 图像2 * 系数2 + 亮度调节量
alpha：系数1 
beta：系数2
gamma：亮度调节量，这个参数不能省略
"""
# 读取图片
src1 = cv2.imread('noise_lena.bmp')
src2 = cv2.imread('test1_lena.bmp')

# 图像融合
result = cv2.addWeighted(src1, 1, src2, 1, 0)

# 显示图像
cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.imshow("result", result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
