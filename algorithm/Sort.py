# -*- coding: utf-8 -*-
# Auther :
# Mail :
# Date : 2022/10/13 20:37
# File : Sort.py


import random
import time
import sys
import numpy as np
sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000

def insertionSort(A):
    '''
    插入排序
    :param A:
    :return:
    '''
    for i in range(1, len(A)):
        x = A[i]
        j = i-1
        while j > -1 and A[j] > x:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x




def bubbleSort(A):
    '''
    冒泡排序
    :param A:
    :return:
    '''
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]








def quickSort(A,low,high):
    '''
    快速排序
    :param A:
    :param low:
    :param high:
    :return:
    '''
    if low < high:
        w = split(A, low-1, high-1)
        quickSort(A, low, w)
        quickSort(A, w+2, high)

def split(A,low,high):
    '''
    划分算法(用于快速排序)
    :param A:
    :param low:
    :param high:
    :return:
    '''
    B = A[low:high+1]
    i = 0
    x = B[0]
    for j in range(1, len(B)):
        if B[j] <= x:
            i = i+1
            if i != j:
                t = B[i]
                B[i] = B[j]
                B[j] = t
    tt = B[0]
    B[0] = B[i]
    B[i] = tt
    A[low:high+1] = B
    return i+low


def to_txt(outputfile,res_list):
    '''
    将结果列表写入文件
    :param res:
    :return:
    '''
    f = open('output\\'+outputfile+'.txt', "w")

    for line in res_list:
        f.write(line + '\n')
    f.close()
    pass


def sortArray(size:int,order:str,algorithm:str,outputfile:str):
    '''
    排序
    :param size:数组大小
    :param order:数组顺序
    :param algorithm:算法名称
    :param outputfile:输出文件名称
    :return:
    '''

    order_set = {'Ascending':[i for i in range(size)],
                 'Descending':[size-i for i in range(size)],
                 'Random':np.random.randint(0,size,size=size),
                 }
    algorithm_set = {'insertionSort':0,
                 'quickSort':1,
                 'bubbleSort':2,
                 }
    try:
        array = order_set[order]
    except KeyError as e:
        print('KeyError:错误的参数',e,'order参数为下列中的一个:Ascending,Descending,Random')
        return

    try:
        fun = algorithm_set[algorithm]
        if fun == 0:
            start_time = time.perf_counter()
            insertionSort(array)
            spend_time = time.perf_counter()-start_time
            res = f'{algorithm},{size},{order},{spend_time},second'
            return res
        if fun == 1:
            start_time = time.perf_counter()
            quickSort(array,1,len(array))
            spend_time = time.perf_counter()-start_time
            res = f'{algorithm},{size},{order},{spend_time},second'
            return res

        if fun == 2:
            start_time = time.perf_counter()
            bubbleSort(array)
            spend_time = time.perf_counter()-start_time
            res = f'{algorithm},{size},{order},{spend_time},second'
            return res
    except KeyError as e:
        print('KeyError:错误的参数',e,'algorithm参数为下列中的一个:insertionSort,quickSort,bubbleSort')
        return




if __name__ == '__main__':
    now = time.perf_counter()
    a = ['insertionSort','bubbleSort','quickSort']
    b = ['Ascending','Descending','Random']
    for i in a:
        for j in b:
            res_list = []
            for s in [10,100,1000,10000]:
                res_list.append(sortArray(s,j,i,outputfile=i))
            to_txt(i+'_'+j, res_list)
    print('运行时间',time.perf_counter()-now)