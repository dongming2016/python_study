#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 20:04

import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import My_Logger

leaf_path = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
root_logger = My_Logger.Logger('root', r'中国银行_爬虫_log.log')
file_patition = input('请输入你想存入的磁盘分区,如c，则输入c, 默认c盘:')
if not file_patition:
    file_patition = 'c'
base_path = '%s:/bank/CB/%s' % (file_patition, leaf_path)

def create_dir(file_path):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        return True
    else:
        print('路径已存在')
        return False

create_dir(base_path)

def get_html(url):
    header={'user-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=header)
    res.encoding='utf-8'
    return  BeautifulSoup(res.text, 'html.parser')

# print(soup.select('.main .news .list li a')[0].get('href'))
# soup.select('.main .news .list li a')
def get_files(html):
    a_tags = html.select('.main .news .list li a')
    for item in a_tags:
        href = item.get('href')
        ss = href.split(r'/')
        root_logger.debug(ss[len(ss) - 1])
        file_name = ss[len(ss) - 1]
        title = item.get_text()
        root_logger.debug(href)
        root_logger.debug(title)
        req = requests.get(href)
        with open(base_path + '/' + file_name, 'wb') as pdf:
            pdf.write(req.content)

def get_next_url(html):
    return html.select('.turn_page .turn_next')

def get_total_page_num(html):
    return html.select('.turn_page p span')[0].get_text()

def get_all_files(url, Number):
    html = get_html(url)
    # print(html.encode('utf-8'))
    total_page_num = get_total_page_num(html)
    # next_url = get_next_url(html)
    # print(total_page_num)
    page_num = 0
    get_files(html)
    while True:
        # print("=====================================================", page_num, Number)
        if page_num > int(total_page_num) or page_num >= Number - 1:
            break
        page_num += 1
        root_logger.debug(url.replace('.html', '') + '_' + str(page_num) + '.html')
        new_url = url.replace('.html', '') + '_' + str(page_num) + '.html'
        root_logger.debug(new_url)
        get_files(get_html(new_url))
    # print(next_url)


if __name__ == '__main__':
    print('==========================================欢迎使用中国银行爬虫小程序！=========================================')
    Number = int(input('请输入【页面】数目：'))
    get_all_files('http://www.boc.cn/fimarkets/cs8/fd6/index.html', Number)