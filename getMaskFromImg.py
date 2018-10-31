#encoding=utf-8
#author:Ethan
#software:Pycharm
#file:getMaskFromImg.py
#time:2018/10/22 上午10:59

import cv2

def getMaskFromImg(image):
    mask = None
    #todo

    return mask
    pass




if __name__ == '__main__':
    image = cv2.imread('./images/fangtianxia.jpg')
    mask = getMaskFromImg(image)
    cv2.imshow('showimage',image)
    cv2.imshow('showmask',mask)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

