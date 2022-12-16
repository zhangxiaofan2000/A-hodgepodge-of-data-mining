""" 用户输入姓名、课程名称和每门课程的成绩，生成10条数据写入myscore.csv文件，然后读取该文件，完成以下任务：
  1.计算每位同学的总分，增加总分列
  2.计算每位同学的平均分，保留两位小数，增加平均分列
  3.计算计算每门课程的平均分，保留两位小数
  4.计算每门课程的最高分
  5.计算每位同学成绩的中位数，保留两位小数
  6.计算每门课程成绩的中位数，保留两位小数
  7.按总分降序排序后写回到文件
  8.以字典的方式分别输出每门课程的平均分、每位同学成绩的中位数、每门课程成绩的中位数和每门课程的最高分
  9.降序输出总分排前三的记录
  10.升序输出平均分排后三的记录

  根据给出的代码和pass语句后的注释要求，写一条语句替换pass语句，实成程序设计。
  数据输入要求：输入至少10条数据
"""
import pandas as pd  # 导入pandas库起别名为pd

data=[]
print('请输入五门课程，用空格分隔')
data_course=input('请输入课程：')
data.append(['姓名']+data_course.split(' '))  # 用户输入切分为列表添加到创建的列表
print('请依次输入姓名和五门课程成绩，用空格分隔')
while True:
    data_score=input('请输入姓名和成绩数据：')
    if data_score=='':
        break  # 用户输入回车退出循环，中止输入
    data.append(data_score.split(' '))  # 用户输入切分为列表添加到创建的列表

with open('./data/myscore.csv','w',encoding='utf-8') as f:
    for x in data:
        f.write(','.join(map(str, x)) + '\n')  # 列表的元素转换为字符串写入文件

file = './data/myscore.csv' # 指定要读取的文件
score = pd.read_csv(file) # 读文件myscore.csv中的数据到dataframe对象中
scoreSum = [sum(x[1:]) for x in score.values.tolist()]  # 计算总分
average_scores = [round(sum(x[1:]) / (len(x) - 1), 2) for x in score.values.tolist()] # 计算每位同学的平均分,保留两位小数
scoreMean_course=round(score.mean(numeric_only=True),2) # 计算每门课程的平均分，保留两位小数
scoreMax_course=score.max(numeric_only=True) # 计算每门课程的最高分
scoreMedian_student=round(score.median(axis=1,numeric_only=True),2) # 计算每位同学成绩的中位数，保留两位小数
scoreMedian_course= round(score.median(axis=0,numeric_only=True),2) # 计算每门课程成绩的中位数，保留两位小数
print(dict(scoreMean_course)) # 用字典的方式输出每门课程的平均分
print(dict(scoreMedian_student)) # 用字典的方式输出每位同学成绩的中位数
print(dict(scoreMedian_course)) # 用字典的方式输出每门课程成绩的中位数
print(dict(scoreMax_course)) # 用字典的方式输出每门课程的最高分
score['总分'] = scoreSum              # 在数据最后加上总分列
score['平均分'] = average_scores   # 在数据最后加上平均分列
score = score.sort_values(by=['总分'], ascending=False)  # 总分降序排序
score.to_csv(file) # 写回到文件

print(score.sort_values('总分', ascending=False)[:3]) # 降序输出总分排前三的记录
print(score.sort_values('平均分', ascending=True)[-3:])  # 升序输出平均分排后三的记录



'''
Python Java C++ 数学 语文

小张 90 80 60 90 80
小王 76 65 60 90 80
小李 84 89 60 78 80
小钱 75 87 89 90 96
小松 90 80 60 90 42
小梅 95 80 80 90 56
小赵 100 80 60 90 96
靓仔 100 100 100 100 100
'''
        
        


