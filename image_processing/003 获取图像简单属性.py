import cv2


img = cv2.imread('../images/lena.bmp')
#通过shape获得图像的形状，其中灰度图像返回行数、列数，彩色图像返回行数、列数和通道数
print(img.shape)

#通过size获取图像的像素数目，其中灰度图像返回行数*列数，彩色图像返回行数*列数*通道数
print(img.size)

#通过dtype获得图像的数据类型，通常返回uint8
print(img.dtype)


cv2.imshow('lena',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

