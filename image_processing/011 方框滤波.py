import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
方框滤波
result = cv2.boxFilter(原始图像，目标图像深度，核大小，normalize属性)
其中图像深度是int类型，通常用-1表示与原始图像一致
核大小是以(宽度，高度)表示的元祖形式，常见的是（3,3,）,（5,5）
normalize属性表示对目标图像是否进行归一化处理，当为true时进行均值化处理，false时不进行均值化处理。
实际上为求周围的像素之和，很容易发出溢出，溢出时为白色，对应的像素为255
"""

img = cv2.imread('noise_lena.bmp',cv2.IMREAD_UNCHANGED)
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#方框滤波
#采用(5,5)的核，normalize=1表示进行归一化处理，此时与均值滤波相同
result = cv2.boxFilter(source,-1,(5,5),normalize=1)

#显示图像
title = ['Source Image','BoxFilter Image']
images = [source,result]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(title[i])
plt.show()


#显示图像左上角处理前后的像素
print(source[0:3,0:3,0])
print(result[0:3,0:3,0])

