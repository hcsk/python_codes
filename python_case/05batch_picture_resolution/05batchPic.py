#coding=utf-8

'''
遍历目录下所有图片,使用PIL库进行处理,分辨率变为640*1136(IPhone5屏幕分辨率)
'''

import Image,os

inPath=os.getcwd()+'/media/'
outPath=os.getcwd()+'/media/'

def processImage(file_in,file_out,name,imgType):
    '''

    :param file_in:存放原始照片的目录
    :param file_out: 输出目录
    :param name: 文件名
    :param imgType: 文件类型
    :return:
    '''
    imgType='jpeg' if imgType=='.jpg' else 'png'    #true_part if condition else false_part 类似三元运算符 imgType=imgType=='.jpg'?'jpeg':'png'

    img=Image.open(file_in+name)

    #缩放比例
    rate=max(img.size[0]/640.0 if img.size[0]>640 else 0, img.size[1]/1136.0 if img.size[1]>1136 else 0)
    if rate:
        img.thumbnail((img.size[0]/rate, img.size[1]/rate))
    img.save(file_out+'out_'+name,imgType)

def run():
    '''切换到数据目录,遍历目录下的所有图片'''
    os.chdir(inPath)
    for i in os.listdir(os.getcwd()):
        postfix=os.path.splitext(i)[1]
        if postfix=='.jpg' or postfix=='.png':
            processImage(inPath,outPath,i,postfix)

if __name__ == '__main__':
   run()