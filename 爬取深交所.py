# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/9/29 20:38
# File : 爬取深交所.py

'''
爬取深圳证券交易所财报地址
每一页有30个财报
每10页手动保存一次,防止被发现
'''
import requests
import time
import pandas as pd
import random
import os
import json


# 定义爬取函数
def get_pdf_address(pageNum):
    url = 'http://www.szse.cn/api/disc/announcement/annList?random=%s' % random.random()
    # headers= {'User-Agent':str(UserAgent().random)}

    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01'
        , 'Accept-Encoding': 'gzip, deflate'
        , 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        , 'Content-Type': 'application/json'
        , 'Host': 'www.szse.cn'
        , 'Origin': 'http://www.szse.cn'
        , 'Proxy-Connection': 'close'
        , 'Referer': 'http://www.szse.cn/disclosure/listed/fixed/index.html'
        ,
               'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.169 Safari/537.36'
        , 'X-Request-Type': 'ajax'
        , 'X-Requested-With': 'XMLHttpRequest'}

    pagenum = int(pageNum)
    payload = {"seDate": ["2020-01-01", "2020-12-31"], "channelCode": ["fixed_disc"], "bigCategoryId": ["010303"],
               "pageSize": 30, "pageNum": pagenum}
    response = requests.post(url, headers=headers, data=json.dumps(payload))  # 使用json格式
    result = response.json()
    return result


# 创建一个DataFrame储存爬取信息
pdf_infor = pd.DataFrame(columns=['secCode', 'secName', 'url', 'title', 'publishTime'])

# 下载域名的前缀
count = 0
url_head = 'http://disc.static.szse.cn/download/'

# 起始页数时page_a,我一次只爬了10页,所以截至页数是page_b = page_a + 10
page_a = 150
page_b = page_a + 10

path_xlsx = 'download_url_' + str(page_a) + '_' + str(page_b - 1) + '.xlsx'  # 保存为excel的文件名

for i in range(page_a, page_b):

    print("爬取深交所年报下载地址第{}页".format(i))
    result = get_pdf_address(i)
    num = len(result['data'])
    for each in range(num):
        # each = 1
        pdf_infor.at[count, 'secCode'] = result['data'][each]['secCode'][0]
        pdf_infor.at[count, 'secName'] = result['data'][each]['secName'][0]
        pdf_infor.at[count, 'url'] = url_head + result['data'][each]['attachPath']
        pdf_infor.at[count, 'title'] = result['data'][each]['title']
        pdf_infor.at[count, 'publishTime'] = result['data'][each]['publishTime']
        count += 1
    print('获取完成')
    time.sleep(random.uniform(2, 3))  # 控制访问速度

# 提取title中字符串获取年份
pdf_infor['Year'] = pdf_infor['title'].str.extract('([0-9]{4})')
pdf_infor.to_excel(path_xlsx)  # 保存为excel