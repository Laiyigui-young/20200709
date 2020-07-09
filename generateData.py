#!/usr/bin/python
#coding=utf-8
#@Time      :2020/7/6 11:54
#@Author    :Laiyigui
#@File      :hash.py

#服务器中使用的时候需要添加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random

def generateData(num):
    data = set()
    while (len(data) < num):
        data.add(random.randint(1, num*10))
    # f = open(pathname,"w")
    # for i in data:
    #    f.write(str(i)+'\n')
    # f.close()
    return list(data)

if __name__ == '__main__':
    num = 10
    a = generateData(num)
    b = generateData(num)
