# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/9/29 20:59
# File : A股爬取.py
import json
import requests
import re
import datetime
import csv
f=open ('stkcd.csv',mode='w',encoding='gbk',newline='')
writer = csv.writer(f)
head=['stkcd']
writer.writerow(head)
#要下载的年报日期可以根据需要调整，开始日期和结束日期间隔最好不要超过30日#

for year in range(2000)
begin = datetime.date(2019,1,19)
end = datetime.date(2019,6,21)
for i in range((end - begin).days+1):
    searchDate = str(begin + datetime.timedelta(days=i))
    response=requests.get(
        'http://query.sse.com.cn/infodisplay/queryLatestBulletinNew.do?&jsonCallBack=jsonpCallback43752&productId=&reportType2=DQGG&reportType=YEARLY&beginDate='+searchDate+'&endDate='+searchDate+'&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1561094157400',
        headers={'Referer':'http://www.sse.com.cn/disclosure/listedinfo/regular/'}
    )
    json_str = response.text[19:-1]
    data = json.loads(json_str)
    for report in data['result']:
        download_url = 'http://www.sse.com.cn/' + report['URL']
        if re.search('年度报告',report['title'],re.S):
            if re.search('摘要',report['title'],re.S):###避免下载一些年报摘要等不需要的文件###
                pass
            else:
                filename = '爬取文件/'+report['security_Code']+report['title'] +searchDate+ '.pdf'
                print(filename)
                writer.writerow([report['security_Code']])###将公司代码写进csv文件，便于计数，非必须步骤###
                if re.search('ST',report['title'],re.S):###下载前要将文件名中带*号的去掉，因为文件命名规则不能带*号，否则程序会中断###
                    filename='爬取文件/'+report['security_Code']+'-ST' +searchDate+ '.pdf'
                    download_url = 'http://static.sse.com.cn/' + report['URL']
                    resource = requests.get(download_url, stream=True)
                    with open(filename, 'wb') as fd:
                        for y in resource.iter_content(102400):
                            fd.write(y)
                        print(filename, '完成下载')
                else:
                    download_url = 'http://static.sse.com.cn/' + report['URL']
                    resource = requests.get(download_url, stream=True)
                    with open(filename, 'wb') as fd:
                        for y in resource.iter_content(102400):
                            fd.write(y)
                        print(filename, '完成下载')

