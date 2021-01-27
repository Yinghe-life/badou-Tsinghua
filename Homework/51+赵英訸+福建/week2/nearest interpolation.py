import cv2
import numpy as np

def nearestinterp(img,h,w):
    '''
    :param img: 原始图像取样值
    :param h: 目标图像的高度
    :param w: 目标图像的宽度
    :return:目标图像
    '''
    height,width,channels = img.shape
    empty_image = np.zeros((h,w,channels),np.uint8)
    scale_h = height/h
    scale_w = width/w
    for i in range(h):
        for j in range(w):
            x = int(i*scale_h)
            y = int(j*scale_w)
            empty_image[i][j] = img[x][y]
    return empty_image

image = cv2.imread('lenna.png')
image_change = nearestinterp(image,400,800)
print(image_change.shape)
cv2.imshow('nearest interp',image_change)
cv2.imshow('lenna',image)
cv2.waitKey(0)
