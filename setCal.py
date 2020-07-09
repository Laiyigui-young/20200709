#!/usr/bin/python
#coding=utf-8
#@Time      :2020/7/6 11:54
#@Author    :Laiyigui
#@File      :hash.py

#服务器中使用的时候需要添加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import argparse
from generateData import generateData
from hash import hash
from binary import binary
from search import search
from python import python

def calculate(args):
    # 生成数据
    num = int(args.num)
    a = generateData(num)
    b = generateData(num)

    # 交集计算
    interHash,tHash = hash(a,b)
    interBina,tBina = binary(a,b)
    interSear,tSear = search(a,b)
    interPython,tPython = python(a,b)

    # 结果输出
    print("Hash:%f"%tHash)
    print("Bina:%f"%tBina)
    print("Sear:%f"%tSear)
    print("Python:%f"%tPython)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="求解交集的若干方法比较", description="help info.")
    parser.add_argument("--num", default=100, help="数据量大小")
    args = parser.parse_args()
    calculate(args)