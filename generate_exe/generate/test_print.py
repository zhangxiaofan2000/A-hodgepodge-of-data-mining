# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/10/13 13:18
# File : test_print.py
import os
import time

if __name__ == '__main__':
    start = time.perf_counter()
    print('hello')
    a = input('请输入')

    print(a)
    print('运行时间:',time.perf_counter()-start,'s')

    os.system("pause")
