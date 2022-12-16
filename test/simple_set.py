def fil_lst(n,m,k):
    """接收三个正整数参数，以列表的方式返回各位数字互不相同、所有数字之和等于m，并且这个数是k的倍数的n位数
    """
    result = []
    for i in range(10 ** (n - 1), 10 ** n):
        digits = [int(d) for d in str(i)]
        if len(set(digits)) == n and sum(digits) == m and i % k == 0:
            result.append(i)
    return result



if __name__ == '__main__':
    # 调用函数，返回各位数字互不相同、所有数字之和等于5，并且这个数是7的倍数的3位数
    result = fil_lst(3, 5, 7)
    print(result)

