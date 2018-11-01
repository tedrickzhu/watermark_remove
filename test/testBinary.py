#encoding=utf-8
#author:Ethan
#software:Pycharm
#file:testBinary.py
#time:2018/10/22 下午2:57

'''
想法：
1将原始的彩图灰度化之后，
2选择合适的阈值二值化，这样，水印位置将会比较明显，
3再采用模板匹配，定位出图片中多个水印的位置

问题：不同位置的水印，他们的背景的像素值差异比较大，
水印位置的像素值是根据公式pixl=s*a+(1-a)*w,
水印蒙版w一般都是255固定的，透明度a也是固定的。
所以，添加水印后的pixl值与背景图成正相关，
所以采用单一的阈值做二值化后的图片会完全丢失一部分水印的信息
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

def gray2binary(GrayImage):

    ret,thresh1=cv2.threshold(GrayImage,130,255,cv2.THRESH_BINARY)
    ret,thresh2=cv2.threshold(GrayImage,130,255,cv2.THRESH_BINARY_INV)
    ret,thresh3=cv2.threshold(GrayImage,130,255,cv2.THRESH_TRUNC)
    ret,thresh4=cv2.threshold(GrayImage,130,255,cv2.THRESH_TOZERO)
    ret,thresh5=cv2.threshold(GrayImage,130,255,cv2.THRESH_TOZERO_INV)
    titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in xrange(6):
       plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()

def gray2binary2(GrayImage):
    for i in range(0,GrayImage.shape[0]):
        for j in range(0,GrayImage.shape[1]):
            if GrayImage[j][i]<200:
                GrayImage[j][i]=0

            # print('change value')
    res = np.float32(GrayImage)
    pass

if __name__ == '__main__':

    # img=cv2.imread('./mask/5i5j-logo.bmp')
    img=cv2.imread('./../data/jpg/100000.jpg')
    print(type(img), img.shape)
    # GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image',GrayImage)
    # gray2binary(GrayImage)
