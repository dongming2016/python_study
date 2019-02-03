#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 20:04

import  requests
from bs4 import BeautifulSoup

header={'user-agent': 'Mozilla/5.0'}
res = requests.get('http://www.yingjiesheng.com/commend-parttime-1.html', headers=header)
res.encoding='gbk'
soup=BeautifulSoup(res.text, 'html.parser')
for job in soup.select('.bg_1'):
    print(job.text)

