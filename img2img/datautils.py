#encoding=utf-8
#author:Ethan
#software:Pycharm
#file:datautils.py
#time:2018/11/1 上午11:04

import cv2
import os
import numpy as np
from PIL import Image

'''
利用Image库进行图片大小的调整，添加水印等操作
'''
def addLogo_anjuke(path,wmpath,cleanpath,dirtypath):
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
def addLogo_5i5jfull(path,wmpath,originpath,dirtypath):
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

'''
缩小原图的大小，将logo图调整到与小图一致，然后添加进去
'''
def resize_addwm_5i5jfull(path,wmpath,originpath,dirtypath):
    watermark = cv2.imread(wmpath)
    logoname = wmpath.split('/')[-1].split('.')[0]
    # print(logoname)
    # print(watermark.shape)
    # filelist = os.listdir(os.getcwd()+os.sep+"data/jpg")
    filelist = os.listdir(path)
    #提取出n张图片
    count= 0
    for filename in filelist:
        # if filename != '105104.jpg':
        #     continue
        # print(filename)
        # if count >= 2000:
        #     break
        image = cv2.imread(path+filename)
        print(path+filename)
        #将原图缩小,最大为400
        img_h ,img_w = image.shape[0],image.shape[1]
        rate = max(img_h,img_w)//400.0
        if rate > 0.0:
            rate = rate+1.0
            image = cv2.resize(image, (int(img_w / rate), int(img_h / rate)))
        #将水印图调整到与小图一致
        img_h, img_w = image.shape[0], image.shape[1]
        watermark_res = cv2.resize(watermark,(img_w, img_h))
        mask = np.floor(watermark_res.astype(np.float32) * 0.3).astype(np.uint8)
        imageadd2 = cv2.add(image,mask)

        # imageaddweight = cv2.addWeighted(image,0.9,watermark,0.2,0)
        # imagescaleadd = cv2.scaleAdd(image,0.9,watermark,0.2)

        if not os.path.exists(originpath):
            os.makedirs(originpath)
        if os.path.exists(originpath+logoname+'_'+filename):
            print(originpath+logoname+'_'+filename,' this origin file has exists')
            # cv2.imwrite(originpath+filename,image)
        else:
            cv2.imwrite(originpath+logoname+'_'+filename,image)

        if not os.path.exists(dirtypath):
            os.makedirs(dirtypath)
        if os.path.exists(dirtypath + logoname+'_'+filename):
            print(dirtypath + logoname+'_'+filename,' this dirty file has exists')
        else:
            cv2.imwrite(dirtypath + logoname+'_'+filename, imageadd2)
        count+=1
        # cv2.imshow('origin', image)
        # cv2.imshow('add2', imageadd2)
        # cv2.waitKey(0)
        # break
    pass


if __name__ == '__main__':
    data = '../../data/jpg2/'
    wmpath = '../mask/fang_mask.jpeg'
    originpath = '../images/data/origin/'
    dirtypath = '../images/data/dirty/'

    # addLogo_5i5jfull(data,wmpath,originpath,dirtypath)
    resize_addwm_5i5jfull(data,wmpath,originpath,dirtypath)
