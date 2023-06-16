import cv2
import numpy as np
import matplotlib.pyplot as plt

"""

"""

img = cv2.imread('../images/lena.bmp',cv2.IMREAD_UNCHANGED)
test = img

#第一种方法
res1 = img + test
#第二种方法
res2 = cv2.add(img,test)

cv2.imshow('original',img)
cv2.imshow('res1',res1)
cv2.imshow('res2',res2)

cv2.waitKey(0)
cv2.destroyAllWindows()
