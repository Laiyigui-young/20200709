#!/usr/bin/python
# -*- coding:UTF-8 -*-
#@Time      :2020/7/6 11:54
#@Author    :Laiyigui
#@File      :hash.py

#服务器中使用的时候需要添加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
def hash(a,b):
    # 基于字典的求解算法
    # 除法取余法实现的哈希函数
    def myHash(data,hashLength):
        return data % hashLength

    # 哈希表检索数据
    def hashSearch(hash,hashLength,data):
        hashAddress=myHash(data,hashLength)
       #指定hashAddress存在，但并非关键值，则用开放寻址法解决
        while hash.get(hashAddress) and hash[hashAddress]!=data:
            hashAddress+=1
            hashAddress=hashAddress%hashLength
        if hash.get(hashAddress)==None:
            return -1
        return hashAddress

    #数据插入哈希表
    def insertHash(hash,hashLength,data):
        hashAddress=myHash(data,hashLength)
        #如果key存在说明应经被别人占用， 需要解决冲突
        while(hash.get(hashAddress)):
            #用开放寻址法
            hashAddress+=1
            hashAddress=myHash(hashAddress,hashLength)
        hash[hashAddress]=data


    hashLength = len(a)*2 if len(a)>len(b) else len(b)*2#根据数据量来定，一般定为n或者2n，保证空间复杂度为O(n)
    hashB = {}
    # hashA = {}
    # for i in a:
    #     insertHash(hashA, hashLength, i)


    for i in b:
        insertHash(hashB, hashLength, i)

    # 交集计算
    t1 = time.time()
    inter = []
    for i in a:
        result = hashSearch(hashB,hashLength, i)
        if result!=-1:
            inter.append(i)

    t2 = time.time()
    # 返回值
    return sorted(inter),t2-t1