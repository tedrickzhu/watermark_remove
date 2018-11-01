#encoding=utf-8
#author:Ethan
#software:Pycharm
#file:datautils.py
#time:2018/11/1 上午11:04

import cv2
import os
import numpy as np
from PIL import Image

def addLogo(path,wmpath):
    watermark = Image.open(wmpath)
    print(watermark.size)
    # filelist = os.listdir(os.getcwd()+os.sep+"data/jpg")
    filelist = os.listdir(path)
    for filename in filelist:
        image = Image.open(path+filename)
        print(image.size)

        break
    pass

'''
1，缩小原图的大小，以logo图片的尺寸为标准，小图片可以加速计算，存为原始图片origin
2，将logo加入到origin中，生成有水印图片，存为dirty
'''
def addLogo_cv2(path,wmpath,originpath,dirtypath):
    watermark = cv2.imread(wmpath)
    watermark = cv2.resize(watermark,(watermark.shape[1]/2,watermark.shape[0]/2))
    wm_w,wm_h = watermark.shape[1],watermark.shape[0]
    print(wm_w,wm_h)
    # filelist = os.listdir(os.getcwd()+os.sep+"data/jpg")
    filelist = os.listdir(path)
    for filename in filelist:
        image = cv2.imread(path+filename)

        image = cv2.resize(image,(wm_w,wm_h))

        mask = np.floor(watermark.astype(np.float32) * 0.3).astype(np.uint8)
        imageadd2 = cv2.add(image,mask)

        if not os.path.exists(originpath):
            os.makedirs(originpath)
        if os.path.exists(originpath+filename):
            print(originpath+filename,' this origin file has exists')
            # cv2.imwrite(originpath+filename,image)
        else:
            cv2.imwrite(originpath+filename,image)

        if not os.path.exists(dirtypath):
            os.makedirs(dirtypath)
        if os.path.exists(dirtypath + filename):
            print(dirtypath + filename,' this dirty file has exists')
        else:
            cv2.imwrite(dirtypath + filename, imageadd2)

        # print(watermark.shape,image.shape)
        # cv2.imshow('origin',image)
        # cv2.imshow('add2',imageadd2)
        # cv2.waitKey(0)
        break
    pass


def resize_addwm(path,wmpath):
    watermark = cv2.imread(wmpath)
    print(watermark.shape)
    # filelist = os.listdir(os.getcwd()+os.sep+"data/jpg")
    filelist = os.listdir(path)
    for filename in filelist:
        # print(filename)
        image = cv2.imread(path+filename)

        image = cv2.resize(image,(watermark.shape[1],watermark.shape[0]))
        imageadd = cv2.add(image,watermark)

        mask = np.floor(watermark.astype(np.float32) * 0.3).astype(np.uint8)
        # cv2.imshow('mask',mask)
        imageadd2 = cv2.add(image,mask)
        # imageadd2 = imageadd2 * (imageadd2 <= 255) + 255 * (imageadd2 > 255)
        # imageadd2 = np.floor(imageadd2 * (imageadd2 <= 255) + 255 * (imageadd2 > 255)).astpye(np.uint8)
        # imageadd2 = imageadd2.astpye(np.uint8)

        # imageaddweight = cv2.addWeighted(image,0.9,watermark,0.2,0)
        # imagescaleadd = cv2.scaleAdd(image,0.9,watermark,0.2)
        cv2.imshow('origin',image)
        cv2.imshow('add',imageadd)
        cv2.imshow('add2',imageadd2)
        # cv2.imshow('addweight',imageaddweight)
        # cv2.imshow('scale',imagescaleadd)
        cv2.waitKey(0)
        # print(path+filename)
        print(image.shape)

        break
    pass


if __name__ == '__main__':
    data = '../../data/jpg/'
    wmpath = '../mask/5i5j-logo.bmp'
    originpath = '../images/origin/'
    dirtypath = '../images/dirty/'
    addLogo_cv2(data,wmpath,originpath,dirtypath)

