import cv2
import numpy as np

def bi_inter(img,w,h):
    height,width,channels = img.shape
    empty_image = np.zeros((h, w, channels), dtype=np.uint8)
    if height == h and width == w:
        return img.copy()
    scale_h = float(height / h)
    scale_w = float(width / w)
    for k in range(channels):
        for i in range(h):
            for j in range(w):
                x = (i + 0.5) * scale_h - 0.5
                y = (j + 0.5) * scale_w - 0.5
                x0 = int(np.floor(x))
                y0 = int(np.floor(y))
                x1 = min(x0 + 1, height - 1)
                y1 = min(y0 + 1, width - 1)
                temp0 = (x1 - x)*img[y0,x0,k] + (x - x0)*img[y0,x1,k]
                temp1 = (x1 - x)*img[y1,x0,k] + (x - x0)*img[y1,x0,k]
                empty_image[j, i, k] = int((y1 - y)*temp0 + (y - y0)*temp1)

    return empty_image

image = cv2.imread('lenna.png')
image_change = bi_inter(image,700,700)
print(image_change.shape)
cv2.imshow('bilinear interp',image_change)
cv2.imshow('lenna',image)
cv2.waitKey(0)
