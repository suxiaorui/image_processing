import cv2
#读取图像
img = cv2.imread('../images/lena.bmp')
print(img)
#显示图像
cv2.imshow('lena',img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

#写入图像 在该文件夹下保存了一张名为est_lena.bmp的图像
cv2.imwrite('test_lena.bmp',img)