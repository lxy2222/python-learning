
# -*- coding:utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random
import string
def get_code(num,length = 7):
    filename = "activation_code.txt"
    file = open(filename,"w")
    for i in range(num):
        chars = string.letters + string.digits #激活码由数字和字母组成
        str = [random.choice(chars) for i in range(length)]#默认挑选7个字母来作为激活码
        file.write(''.join(str) + '\n')#用空格作为分隔符，讲str中所有元素合并成一个新的字符串，并且每个字符串换行
    file.close()
get_code(200)
