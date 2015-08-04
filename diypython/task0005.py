# -*-coding:utf-8 -*-
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
from PIL import Image
def changepicture(picfile,result):
    img = Image.open(picfile) #获取图片大小
    x,y = img.size
    changex = float(x)/result[0]
    changey = float(y)/result[1]
    if changex > 1  or  changey > 1:
        change = changex if changex > changey else changey
       # print change
      #  print int(result[0]/change),int(result[1]/change)
        img.resize((int(x/change),int(y/change))).save('result.jpg')#改变图片尺寸后保存图片
if __name__ == 'main':
   changepicture('pic.jpg',(1136,640))





