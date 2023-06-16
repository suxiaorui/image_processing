import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
高斯滤波
result = cv2.GaussianBlur(src,ksize,sigmaX)
其中src表示原始图像，ksize表示核大小，sigmaX表示X方向方差    核大小必须是奇数，X方向方差控制权重
"""

img = cv2.imread('noise_lena.bmp',cv2.IMREAD_UNCHANGED)
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#方框滤波
#如果normalize=0，则不进行归一化处理，像素值为周围像素之和，更多为白色，如果改成(2,2)，只取四个像素可能会好点。
result = cv2.GaussianBlur(source,(3,3),0)

#显示图像
title = ['Source Image','GaussianBlur Image']
images = [source,result]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(title[i])
plt.show()


