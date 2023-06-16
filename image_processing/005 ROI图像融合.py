import cv2
import numpy as np

img = cv2.imread('../images/lena.bmp',cv2.IMREAD_UNCHANGED)

#定义一个200*100的矩阵，3对应BGR
face = np.ones((200,100,3))
#显示原始图像
cv2.imshow('lena',img)

#显示ROI区域，将ROI区域显示在原始图像的左上角
face = img[200:400,200:400]
img[0:200,0:200] = face
cv2.imshow('face',img)

cv2.waitKey(0)
cv2.destroyAllWindows()