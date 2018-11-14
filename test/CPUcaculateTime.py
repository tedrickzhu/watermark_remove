#encoding=utf-8
#time=18-11-6 上午11:36
__author__ = 'Ethan'

'''
对于目标程序，输入输出的图片尺寸必须保持一致，对于本机可以计算200x200的输入输出，batchsize可以为64
或者400*400的输入输出，batchsize为16，过大则机器内存不足，跑不动


n张图片，已经压缩到不大于400像素
batchsize，为了保证输出图片较大，固定为16,则每个epoch需要计算n/batchsize次
epoch,50,100,200，
speed为每个batchsize训练的时间,对于本机的4核CPU一般约为23s
time，训练多少小时需要出结果,单位为小时
则有如下关系：
time=((n/batchsize)*epoch*speed)/3600

所以可以调节图片的数量来控制训练时间：
n = (time*3600*batchsize)/(epoch*speed)
'''

def caculate(batchsize,epoch,n=None,time=None,speed=25):
    if n is not None and time is None:
        # n=5200
        time=((n/batchsize)*epoch*speed)/3600.0
        print('%d张图片，训练%d个epoch需要训练%f小时'%(n,epoch,time))
    if n is None and time is not None:
        # time = 12
        n = (time*3600*batchsize)/(epoch*speed)
        print('训练%d个epoch,训练%d小时，需要%d张图片'%(epoch,time,n))

if __name__ == '__main__':
    batchsize = 16
    epoch = 100
    n = None
    time = 24

    caculate(batchsize=batchsize,epoch=epoch,n=n,time=time)

