import math
# 调用阶乘函数，计算并输出用户输入的20以内的正整数的阶乘。提示信息为：请输入一个20以内的正整数
print(math.factorial(int(input("请输入一个20以内的正整数: "))))


import random,string
# 调用random.choices()方法，随机从ascii字母和数字串中取5个字符生成列表，拼接列表元素为字符串输出
print(''.join(random.choices(string.ascii_letters + string.digits, k=5)))

import os
# 在当前文件夹下创建名为datatxt的文件夹
if not os.path.exists('datatxt'): os.mkdir('datatxt')



set1={'hour':'23','miniute':56,'second':'37'}
# 以':'为分隔符，调用join()方法和map方法输出字典set1的值，输出结果为：23:56:37
print(':'.join(list(map(str, set1.values()))))


student='我的名字叫{},是广东财经大学的学生'.format(input('请输入你的姓名：'))
# 用逆序索引从student切片输出你的姓名,其中姓名输入自己的名字
print(student[-student.rfind('}'):])


lst,tu=[33,44,55,66],(77,88,99)
# 把元组tu解包后添加到列表lst
print(lst.extend(list(tu)))



my_lst=['73','13','9','82','66']
# 对列表my_lst按整数排序，降序输出
print([int(i) for i in my_lst].sort(reverse=True) )

set2={-4,-2,8,4,-6,8,6}
# 取集合set2中大于零的元素并求平方，生成列表输出
print([i**2 for i in [i for i in list(set2) if i > 0]])

class_py,student_no=['审计学2班','审计学2班','行政管理1班'],(56,62,55,77)
# 组合class_py和student_no，生成二元元组合列表并输出，输出结果为：[('审计学2班', 56), ('审计学2班', 62), ('行政管理1班', 55)]
print(list(zip(class_py, student_no)))

s=set(('Python','is','beautiful','?'))
# 用条件表达式实现：如果'?'是集合s元素，删除该元素，如果不是，输出'该元素不存在的信息'
s.discard('?') if '?' in s else print("该元素不存在")






s2019,s2018=['华为','三星','Apple','vivo','oppo'],('三星','Apple','华为','荣耀','wp')
# 用集合返回不同时属于列表s2019和元组s2018的元素，输出结果为：{'wp', 'vivo', 'oppo', '荣耀'}
print(set(s2019).symmetric_difference(set(s2018)))


course={'python': 95, 'Java': 76, 'C语言': 82, '数据库原理': 88}
# 调用update()方法修改数据库原理的成绩为83
course.update({'数据库原理': 83});print(course)



s='  静夜思\n床前明月光,疑是地上霜。\n举头望明月，低头思故乡。\n'
# 去掉首尾空白后将字符串s切分为列表并输出，输出结果为：['静夜思', '床前明月光,疑是地上霜。', '举头望明月，低头思故乡。']
print(s.strip().split('\n'))

with open('./data/poem.txt', 'w', encoding='utf-8') as f:
    # 将字符串'江雪\n千山鸟飞绝，万径人踪灭。\n孤舟蓑笠翁，独钓寒江雪。\n'写入打开的文件
    f.write('江雪\n千山鸟飞绝，万径人踪灭。\n孤舟蓑笠翁，独钓寒江雪。\n')
     
with open('./data/poem.txt', 'r', encoding='utf-8') as f:
    # 读取文件的所有行，每一行去掉换行符后添加到列表data_lst
    print([line.strip() for line in f.readlines()])

import os
# 重命名peom.txt文件为江雪.txt并保存到datatxt文件夹下
if not os.path.exists('./datatxt/江雪.txt'):os.rename('./data/poem.txt', './datatxt/江雪.txt')

import numpy as np
# 从data文件夹下的’8.6 score.csv‘文件获取数据，返回字符串数组
print(np.genfromtxt('./data/8.6 score.csv', dtype=str,encoding="utf8"))

import pandas as pd
# 读取data文件夹下的’8.6 score.csv‘文件的数据，转换为二维列表输出,语句太长可加续行符
print(pd.read_csv('./data/8.6 score.csv').values.tolist())



