#encoding=utf-8

import cv2
import numpy as np

def cam():
    videocap = cv2.VideoCapture(0)
    while videocap.isOpened():
        res,frame = videocap.read()
        # print(frame.shape)
        frame = cv2.resize(frame, (frame.shape[1]/4, frame.shape[0]/4))
        height = frame.shape[0]
        width = frame.shape[1]
        # print('test')
        if res :
            x = cv2.Sobel(frame, cv2.CV_16S, 1, 0)
            y = cv2.Sobel(frame, cv2.CV_16S, 0, 1)

            absx = cv2.convertScaleAbs(x)
            absy = cv2.convertScaleAbs(y)

            dist = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)


            mergeframe = np.zeros((height*2,width*2,3),frame.dtype)
            mergeframe[:height, :width] = frame
            mergeframe[:height, width:] = dist
            mergeframe[height:, :width] = absx
            mergeframe[height:, width:] = absy
            # mergeframe = cv2.resize(mergeframe,(width,height))
            # print(type(frame),type(absx),type(absy),type(dist),type(mergeframe))
            cv2.imshow('source',mergeframe)
            # cv2.imshow('dist',dist)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    videocap.release()
    cv2.destroyAllWindows()

    pass


if __name__ == '__main__':
    cam()