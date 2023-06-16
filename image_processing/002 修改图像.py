import cv2

img = cv2.imread('../images/lena.bmp')
#该区域设置成白色
img[100:200,150:250] = [255,255,255]

cv2.imshow('lena',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('test1_lena.bmp',img)
