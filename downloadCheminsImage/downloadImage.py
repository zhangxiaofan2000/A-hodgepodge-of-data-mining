# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/24 16:32
# File : downloadImage.py
import os

import requests
from bs4 import BeautifulSoup

# 发送HTTP请求获取网页源代码

for i in range(1,8):
    url = 'http://www.chemins-tech.com/cp'+str(i)+'.html'
    response = requests.get(url)
    html_content = response.content




    # 解析网页源代码，获取图片和标题信息
    soup = BeautifulSoup(html_content, 'html.parser')

    title_tag = soup.find('title').string.split('-')[0].strip()
    path = "./image/"+title_tag
    if not os.path.exists(path):
        os.makedirs(path)


    image_tags = soup.find_all('span', class_='coverimg')
    title_tags = soup.find_all('a', class_='tit')

    # 遍历图片和标题信息，下载图片并以标题命名保存
    for i in range(len(image_tags)):
        image_url = image_tags[i]['style'].split("'")[1]
        title = title_tags[i+3].text
        response = requests.get(image_url)
        with open(f'./{path}/{title}.jpg', 'wb') as f:
            f.write(response.content)
