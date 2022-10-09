# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/10/8 20:11
# File : Multiprocessing.py
import concurrent.futures
import multiprocessing
import time
def do_something(seconds):
    print(f'sleeping {seconds} second')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'




if __name__ == '__main__':
    start = time.perf_counter()

    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)
    #
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # processes = []
    # for _ in range(6):
    #     p = multiprocessing.Process(target=do_something,args=(1.5,))
    #     p.start()
    #     processes.append(p)
    # for process in processes:
    #     process.join()


    # ProcessPoolExecutor  ThreadPoolExecutor

    # with concurrent.futures.ProcessPoolExecutor() as exector:
    #
    #     f1 = executor.submit(do_something,1)
    #     f2 = executor.submit(do_something,1)
    #
    #     print(f1.result())
    #     print(f2.result())

    # with concurrent.futures.ProcessPoolExecutor() as exector:
    #     secs = [5,4,3,2,1]
    #
    #     result = [executor.submit(do_something, sec) for sec in secs ]
    #     for f in concurrent.futures.as_completed(result):
    #         print(f.result())

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]

        results = executor.map(do_something,secs)
        for result in results:
            print(result)

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     results = executor.map(do_something, secs)


    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} s')