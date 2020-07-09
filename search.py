#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time      :2020/7/9 10:59
#@Author    :Laiyigui
#@File      :search.py

#服务器中使用的时候需要添加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
def search(a,b):
    t1 = time.time()
    a.sort()#自带的排序算法，时间复杂度为O(nlogn)
    b.sort()#自带的排序算法，时间复杂度为O(nlogn)
    inter = []
    i = 0
    j = 0
    while (i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            i = i+1
        elif(a[i]>b[j]):
            j = j+1
        else:
            inter.append(a[i])
            i = i+1
            j = j+1
    t2 = time.time()
    return inter,t2-t1