# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/10/13 18:52
# File : sort_algorithm.py


import random
import time
import matplotlib.pyplot as plt

def insertionSort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i-1
        while j > -1 and A[j] > x:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x

def merge(A,p,q,r):
    B = list(range(p, r+1))
    s = p
    t = q+1
    k = 1
    while s <= q and t <= r:
        if A[s-1] <= A[t-1]:
            B[k-1] = A[s-1]
            s = s+1
        else:
            B[k-1] = A[t-1]
            t = t+1
        k = k+1
    if s == q+1:
        B[k-1:r:1] = A[t-1:r:1]
    else:
        B[k-1:r:1] = A[s-1:q:1]
    A[p-1:r:1] = B

def bottomupsort(A):
    t = 1
    n = len(A)
    while t < n:
        s = t
        t = 2*s
        i = 0
        while i+t <= n:
            merge(A, i+1, i+s, i+t)
            i = i+t
        if i+s < n:
            merge(A, i+1, i+s, n)

def mergesort(A,low,high):
    if low < high:
        mid = (low+high)//2
        mergesort(A, low, mid)
        mergesort(A, mid+1, high)
        merge(A, low, mid, high)

def split(A,low,high):
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

def quickSort(A,low,high):
    if low < high:
        w = split(A, low-1, high-1)
        quickSort(A, low, w)
        quickSort(A, w+2, high)


X = []
Y1 = []
Y2 = []
Y3 = []
Y4 = []
for i in range(1,8):
    x = 10**i
    print('数量级为', x, '时:')
    X.append(x)
    A = list(range(1, x+1))
    random.shuffle(A)
    B1 = A.copy()
    B2 = A.copy()
    B3 = A.copy()
    B4 = A.copy()

    if i <= 5:
        start = time.time()
        insertionSort(B1)
        end = time.time()
        t = end - start
        print(t)
        Y1.append(t)

    start = time.time()
    bottomupsort(B2)
    end = time.time()
    t = end - start
    print(t)
    Y2.append(t)

    start = time.time()
    mergesort(B3, 1, len(B3))
    end = time.time()
    t = end - start
    print(t)
    Y3.append(t)

    start = time.time()
    quickSort(B4, 1, len(B4))
    end = time.time()
    t = end - start
    print(t)
    Y4.append(t)

x = [i for i in range(1,8)]
x1 = x.copy()
x1.pop()
x1.pop()
plt.plot(x1, Y1, 'ro-', alpha=0.5, label='插入排序')
plt.plot(x, Y2, 'go-', alpha=0.5, label='自底向上排序')
plt.plot(x, Y3, 'bo-', alpha=0.5, label='合并排序')
plt.plot(x, Y4, 'yo-', alpha=0.5, label='快速排序')
plt.xlabel('数量级')
plt.ylabel('运行时间')
plt.xticks(x, X)
plt.legend()
plt.show()

