import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
equalizeHist—直方图均衡化
函数原型： equalizeHist(src, dst=None)
src：图像矩阵(单通道图像)
dst：默认即可
'''

#灰度图像均衡化
#获取灰度图像
img = cv2.imread('lenna.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('image_gray',gray)
#灰度图像直方图均衡化
dst = cv2.equalizeHist(gray)
#直方图
hist = cv2.calcHist([dst],[0],None,[256],[0,256])

plt.figure()
plt.hist(dst.ravel(),256)
plt.show()

cv2.imshow('Histogram Equalization',np.hstack([gray,dst]))
cv2.waitKey(0)

'''
#彩色图像直方图均衡化
img = cv2.imread("lenna.png")
cv2.imshow('src',img)
#彩色图像均衡化前要把每个通道均衡化
(b,g,r) = cv2.split(img)
#直方图均衡化
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
#通道合并
result = cv2.merge((bH,gH,rH))
cv2.imshow('dst_rgb',result)
cv2.waitKey(0)
'''
