# 本程序实现分类统计用户输入的字符串中的字母、数字、中文字符和其他字符的个数。
import string

my_string = input()
letter = 0
digit = 0
chinese = 0
other = 0

for c in my_string:
    if c in string.ascii_letters:
        letter=letter+1
    elif c in string.digits:
        digit+=1
    elif c not in string.printable:
        chinese+=1
    else:
        other += 1
print(letter, digit, chinese,other)



