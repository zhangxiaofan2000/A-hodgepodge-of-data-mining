def is_prime(n):
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False
    减小判定区间，减少循环次数，提升效率。
   
    """
    if n < 2:
        return False      # 0、1、负数以及偶数都不是素数
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:    # 能被2到其根号n之间的整数整除的数不是素数
            return False
    else:
        return True       # for循环正常结束，未遇到return的数是素数

def palindromic(num):
    """接收一个数字为参数，判定其是否为回文数，返回布尔值。
    """
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def reverse_num(num):
    """接收一个整数，返回其逆序字符串对应的整数。
    """
    return int(str(num)[::-1])


def reverse_prime(number):
    """接收一个正整数参数，找出并在同一行内输出所有number位反素数，数字间用一个空格分隔；没有反素数时输出：{number}位数
    没有反素数。
    反素数指某数i及其逆序数都是素数，但数i对应的字符串不是回文字符串，函数无返回值，。
    模块调用用例：输出1位数和4位数的反素数
    """
    #标记变量
    found = False  # 初始化标志变量
    for i in range(10 ** (number - 1), 10 ** number):
        # 将数字i的逆序数记为j
        j = reverse_num(i)
        # 判断i和j是否都是素数，并且i和j的字符串不是回文字符串
        if is_prime(i) and is_prime(j) and not palindromic(i) and not palindromic(j):
            found = True  # 发现了反素数，将标志变量置为True
            print(i, end=' ')
    if not found:  # 未发现反素数
        print(f"{number}位数没有反素数。")




if __name__ == '__main__':
    n = int(input('请输入整数位数：'))
    reverse_prime(n)          # 输出反素数
