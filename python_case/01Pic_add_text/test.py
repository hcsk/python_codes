#coding=utf-8

myPath="./media/"
fontPath="./media/"
inputFile="pic.jpg"
outputFile="output.jpg"

import Image,ImageFont,ImageDraw

#打开图片
img=Image.open(myPath+inputFile)
draw=ImageDraw.Draw(img)

#根据图片大小确定字体大小
fontsize=min(img.size)/4

#添加文字
font=ImageFont.truetype(fontPath+"Phetsarath_OT.ttf",fontsize)
draw.text((img.size[0]-fontsize,0),'sk',font=font,fill=(255,0,0))

img.save(myPath+outputFile,"jpeg")
