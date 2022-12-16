# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/15 14:09
# File : 考试1.py


# 输入一串单词
words = input("请输入一串单词，单词之间用空格隔开: ").split()

# 计算单词的平均长度
average_length = sum(len(word) for word in words) / len(words)

# 筛选出长度大于平均长度的单词
filtered_words = [word for word in words if len(word) > average_length]

# 输出筛选后的单词
print("筛选出长度大于平均长度的单词:", filtered_words)
