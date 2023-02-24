# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/21 10:59
# File : 多线程通信.py
import time
import concurrent.futures
from tqdm import tqdm

def task(n):
     time.sleep(0.1)

n_tasks = 10

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(task, 10) for i in range(n_tasks)]
    for future in tqdm(concurrent.futures.as_completed(futures), total=n_tasks):
        pass
