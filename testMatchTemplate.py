#encoding=utf-8

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

#6种匹配算法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# print(eval('cv2.TM_CCOEFF_NORMED'))#5
# print(cv2.TM_CCOEFF_NORMED)#5

#将上一个max位置矩阵内的值都置为最小值，然后重新找最大值及其位置
def getNextMax(res,max_loc,min_val,h, w):
    for i in range(max_loc[0],min(max_loc[0]+w,res.shape[1])):
        for j in range(max_loc[1],min(max_loc[1]+h,res.shape[0])):
            res[j][i]=min_val
            # print('change value')
    res = np.float32(res)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print('max_val:',max_val)
    return min_val, max_val, min_loc, max_loc,res
    pass


def MultiObjMatch2(image,template):
    print(type(image), image.shape)
    print(type(template), template.shape)
    # image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    h, w = template.shape[0], template.shape[1]
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print('start while')
    while max_val>0.6:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(image, top_left, bottom_right, 255, 2)
        min_val, max_val, min_loc, max_loc ,res= getNextMax(res,max_loc,min_val,h, w)
        print(max_val)

    cv2.imshow('res', res)
    cv2.imshow('compare', image)
    cv2.waitKey(0)
    if 0xFF == ord('q'):
        cv2.destroyAllWindows()
    pass

def MultiObjMatch1(image,template):
    print(type(image), image.shape)
    print(type(template), template.shape)
    # image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    h, w = template.shape[0], template.shape[1]
    # res = cv2.resize(res,(image.shape[1],image.shape[0]))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


    print('maxval:',max_val,'max_loc_val:',res[max_loc[1]][max_loc[0]])
    # print(len(res),len(res[0]))
    print('type of res value:',type(res[0][0]), res.shape)
    print('type of min_val:',type(min_val))
    print('type of min_val convert to numpy:',type(np.float32(min_val)))
    # print('min:', min_val, 'max:', max_val)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, 255, 2)

    res = (res - min_val) / (max_val - min_val)
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] >0.95:
                print(i,j,res[i][j])
                top_left = (j,i)
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv2.rectangle(image, top_left, bottom_right, 255, 2)

    cv2.imshow('res', res)
    cv2.imshow('compare', image)
    cv2.waitKey(0)
    if 0xFF == ord('q'):
        cv2.destroyAllWindows()
    pass

def MatchOne(image,template):
    # w, h = template.shape[::-1]
    h ,w = template.shape[0],template.shape[1]
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    print(type(res), res.shape)
    # print(res)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(type(max_loc), type(max_val))
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(image, top_left, bottom_right, 255, 2)

    cv2.imshow('res', res)
    cv2.imshow('result', image)
    cv2.waitKey(0)
    if 0xFF == ord('q'):
        cv2.destroyAllWindows()

if __name__ == '__main__':
    # image = cv2.imread('./images/fang-864x576-mask.jpg',0)
    # image = cv2.imread('./images/fangtianxia.jpg',0)
    image = cv2.imread('./images/anjuke.jpg',0)
    # template = cv2.imread('./images/fang-mask.jpg',0)
    # template = cv2.imread('./images/fixed-fang-mask.jpg',0)
    template = cv2.imread('./images/ajk-logo2.jpg',0)
    # print(template.shape,image.shape)
    # MultiObjMatch(image,template)
    MatchOne(image,template)

# plt.subplot(221), plt.imshow(image, cmap="gray")
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(222), plt.imshow(template, cmap="gray")
# plt.title('template Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(223), plt.imshow(res, cmap="gray")
# plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(image, cmap="gray")
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.show()