import cv2
import  numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.bmp')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

'''
res = cv2.flip(src,flipCode)
src是指原始图像，flipCode是指翻转方向，如果为0，则表示以X为对称轴翻转，如果大于0，则表示
以Y为对称轴翻转，如果小于0，则表示在X轴、Y轴方向同时翻转
'''

res1 = cv2.flip(img,0)
res2 = cv2.flip(img,-1)
res3 = cv2.flip(img,1)

titles = ['Source','res1','res2','res3']
images = [img,res1,res2,res3]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()