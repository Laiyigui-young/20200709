#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time      :2020/7/9 10:50
#@Author    :Laiyigui
#@File      :binary.py

#服务器中使用的时候需要添加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
def binary(a,b):
    # 二分查找算法
    def binarySearch(lis, num):
        left = 0
        right = len(lis) - 1
        while left <= right:   #循环条件
            mid = (left + right) // 2   #获取中间位置，数字的索引（序列前提是有序的）
            if num < lis[mid]:  #如果查询数字比中间数字小，那就去二分后的左边找，
                right = mid - 1   #来到左边后，需要将右变的边界换为mid-1
            elif num > lis[mid]:   #如果查询数字比中间数字大，那么去二分后的右边找
                left = mid + 1    #来到右边后，需要将左边的边界换为mid+1
            else:
                return mid  #如果查询数字刚好为中间值，返回该值得索引
        return -1  # 如果循环结束，左边大于了右边，代表没有找到

    t1 = time.time()
    a.sort()#自带的排序算法，时间复杂度为O(nlogn)
    b.sort()#自带的排序算法，时间复杂度为O(nlogn)
    inter = []
    for i in a:
        if binarySearch(b, i)!=-1:
            inter.append(i)
    t2 = time.time()
    return inter,t2-t1