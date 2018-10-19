#encoding=utf-8

import cv2
import numpy as np

image = cv2.imread('lianjia.jpg')
# new1 = cv2.GaussianBlur(image,(11,11),15)
# new2 = cv2.GaussianBlur(image,(5,5),10)
#
# cv2.imshow('image',image)
# cv2.imshow('new1',new1)
# cv2.imshow('new2',new2)
#
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #锐化
# dst = cv2.filter2D(new1, -1, kernel=kernel)
#
# cv2.imshow('sharp',dst)
print(image.shape)
mini = cv2.resize(image,(image.shape[0]/5,image.shape[1]/5))
cv2.imshow('minimage',mini)
rebigger = cv2.resize(mini,(mini.shape[0]*5,mini.shape[1]*5))
cv2.imshow('rebigger',rebigger)

cv2.waitKey(0)