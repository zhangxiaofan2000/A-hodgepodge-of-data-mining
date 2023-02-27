# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/24 17:39
# File : excel_to_js.py
import pandas as pd
import string

# 读取 Excel 文件
df = pd.read_excel('数据demo(1).xlsx')

# 将列名转换为小写并替换空格为下划线
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 创建一个空列表
locations = []

# 迭代每一行数据并将其转换为所需格式
for index, row in df.iterrows():
    longitude = row['经度']
    latitude = row['纬度']
    title = row['名称']
    position = [longitude, latitude]
    location = '{position: ' + str(position) + ', title: ' + "'" + title + "'},\n"
    locations.append(location)

# 将列表中的每个元素连接起来，并去掉最后一个逗号
result = ''.join(locations)[:-1]

# 输出结果
print(result)
