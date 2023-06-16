import cv2
import numpy as np

img = cv2.imread('../images/lena.bmp',cv2.IMREAD_UNCHANGED)
rows,cols,chn = img.shape

#拆分通道        提取B颜色通道，将G、R设置成0
b = cv2.split(img)[0]
g = np.zeros((rows,cols),dtype=img.dtype)
r = np.zeros((rows,cols),dtype=img.dtype)

#合并通道
m = cv2.merge([b,g,r])
cv2.imshow('merge',m)


cv2.waitKey(0)
cv2.destroyAllWindows()
