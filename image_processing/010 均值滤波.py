import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
均值滤波
result = cv2.blur(原始图像，核大小)
核大小是以(宽度，高度)表示的元祖形式，常见的是（3,3,）,（5,5）
"""

img = cv2.imread('noise_lena.bmp',cv2.IMREAD_UNCHANGED)
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#均值滤波
result = cv2.blur(source,(1,1))

#显示图像
title = ['Source Image','Blur Image']
images = [source,result]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(title[i])
plt.show()



