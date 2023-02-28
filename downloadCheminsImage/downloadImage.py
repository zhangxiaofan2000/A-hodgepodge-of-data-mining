# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/24 16:32
# File : downloadImage.py
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

#http://www.chemins-tech.com
#https://en.chemins-tech.com


#传感器种类 中文为7种，英文为6种
num = 7
num = num+1
for page in tqdm(range(1,num)):
    # 发送HTTP请求获取网页源代码
    url = 'http://www.chemins-tech.com/cp'+str(page)+'.html'
    response = requests.get(url)
    html_content = response.content

    # 解析网页源代码，获取图片和标题信息
    soup = BeautifulSoup(html_content, 'html.parser')

    title_tag = soup.find('title').string.split('-')[0].strip()
    path = "./image/"+title_tag
    if not os.path.exists(path):
        os.makedirs(path)

    # 查找多个页面
    pagination = soup.find('ul', class_='pagination')
    if pagination:

        # page_links = pagination.find_all('a')
        # page_links = [link.get('href') for link in page_links]
        # page_links = list(set(page_links))  # 去重

        # 遍历所有页面
        for page_link in range(1,len(pagination.find_all('a'))+1):
            url = url+'?orderway=desc&page=' +str(page_link)
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')

            image_tags = soup.find_all('span', class_='coverimg')
            title_tags = soup.find_all('a', class_='tit')

            # 遍历图片和标题信息，下载图片并以标题命名保存
            for i in range(len(image_tags)):
                image_url = image_tags[i]['style'].split("'")[1]
                title = title_tags[i+3].text
                response = requests.get(image_url)
                with open(f'./{path}/{title}.jpg', 'wb') as f:
                    f.write(response.content)
    else:
        # 只有一个页面的情况
        image_tags = soup.find_all('span', class_='coverimg')
        title_tags = soup.find_all('a', class_='tit')

        # 遍历图片和标题信息，下载图片并以标题命名保存
        for i in range(len(image_tags)):
            image_url = image_tags[i]['style'].split("'")[1]
            title = title_tags[i+3].text
            response = requests.get(image_url)
            with open(f'./{path}/{title}.jpg', 'wb') as f:
                f.write(response.content)

