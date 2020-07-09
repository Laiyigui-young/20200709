#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time      :2020/7/9 11:14
#@Author    :Laiyigui
#@File      :python.py

#服务器中使用的时候需要添加
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
def python(a,b):
    t1 = time.time()
    inter = sorted(list(set(a).intersection(set(b))))
    t2 = time.time()
    return inter,t2-t1