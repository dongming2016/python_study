#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 20:04

import requests
from bs4 import BeautifulSoup
import os
base_path = 'c:/bank'

def create_dir(file_path):
    if not os.path.exists(base_path):
        os.mkdir(base_path)
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
        print(ss[len(ss) - 1])
        file_name = ss[len(ss) - 1]
        title = item.get_text()
        print(href)
        print(title)
        req = requests.get(href)
        with open(base_path + '/' + file_name, 'wb') as pdf:
            pdf.write(req.content)

def get_next_url(html):
    return html.select('.turn_page .turn_next')

def get_total_page_num(html):
    return html.select('.turn_page p span')[0].get_text()

def get_all_files(url):
    html = get_html(url)
    # print(html.encode('utf-8'))
    total_page_num = get_total_page_num(html)
    # next_url = get_next_url(html)
    # print(total_page_num)
    page_num = 0
    get_files(html)
    while True:
        page_num += 1
        print(url.replace('.html', '') + '_' + str(page_num) + '.html')
        new_url = url.replace('.html', '') + '_' + str(page_num) + '.html'
        print(new_url)
        get_files(get_html(new_url))

        if page_num > int(total_page_num):
            break
    # print(next_url)


if __name__ == '__main__':
    get_all_files('http://www.boc.cn/fimarkets/cs8/fd6/index.html')