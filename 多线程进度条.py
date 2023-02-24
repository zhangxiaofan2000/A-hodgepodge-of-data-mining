# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/21 11:11
# File : 多线程进度条.py


import concurrent.futures
import time
from tqdm import tqdm

def do_work(x):
    time.sleep(1)
    return x ** 2

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        tasks = range(1, 21)
        results = list(tqdm(executor.map(do_work, tasks), total=len(tasks)))
    print(results)

if __name__ == '__main__':
    main()




'''
方法二
'''

#
# import concurrent.futures
# import time
#
# from tqdm import tqdm
#
# #任务列表 传入的参数
# total_task=[ i for i in range(1000)]
# # 创建进度条，total 为总任务数
# pbar = tqdm(total=len(total_task))
# # 定义要执行的任务
# def do_something(n):
#     time.sleep(0.5)  # 模拟任务耗时 1 秒
#     # 在进度条上更新任务进度
#     pbar.update(1)
#     return n ** 2
#
#
#
#
# # 多线程执行任务
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = list(executor.map(do_something, total_task))
#     pbar.close()  # 关闭进度条