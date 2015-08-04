# -*- coding:utf-8 -*-
#统计一篇英文文档中的单词的个数
import re
def count(filename):
    f = open(filename,'r')
    str = f.read()#读取文本内容
    rules = r'[a-zA-Z0-9]+'#用于匹配的正则表达式
    pattern = re.compile(rules,re.S)
    words = re.findall(pattern,str)
    return len(words)
print count('content_test.txt')
