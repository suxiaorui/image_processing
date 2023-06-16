import cv2
import numpy as np

img = cv2.imread('../images/lena.bmp',cv2.IMREAD_UNCHANGED)
rows,cols,chn = img.shape

#加噪声
for i in range(5000):
    x = np.random.randint(0,rows)
    y = np.random.randint(0,cols)
    img[x,y,:] = [255,255,255]

cv2.imshow('noise',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('noise_lena.bmp',img)