import cv2
import numpy as np

img = cv2.imread('../images/lena.bmp',cv2.IMREAD_UNCHANGED)

#拆分通道
b,g,r = cv2.split(img)

#合并通道
m = cv2.merge([b,g,r])
cv2.imshow('merge',m)

#如果像下面这么写，则合并出来不一样，因为Opencv是按照BGR进行读取的
# m = cv2.merge([g,b,r])
# cv2.imshow('merge',m)


cv2.waitKey(0)
cv2.destroyAllWindows()
