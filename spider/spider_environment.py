#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 20:04

import requests
from bs4 import BeautifulSoup
import xlwt
import os
import json
import re
from datetime import datetime
import math


BASE_URL = 'http://www.mee.gov.cn/xxgklssj/73/index_6709_%s.html'
INIT_URL = 'http://www.mee.gov.cn/xxgklssj/73/index_6709.html'
DOMAIN_URL = 'http://www.mee.gov.cn/%s'

def create_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        return True
    else:
        return False

# 向excel中写表头
def write_head(worksheet, heads):
    col_num = 0
    for head in heads:
        worksheet.write(0, col_num, head)
        col_num += 1


# 向excel中写表体
def write_row(worksheet, row_content):
    row_index = 0

    for row in row_content:
        row_index += 1
        col_index = 0
        for cell in row:
            worksheet.write(row_index, col_index, cell)
            col_index += 1


# 获得标题和链接
def get_content(html, all_content):
    trs = html.select('.iframe-list tr')
    all_data = []
    for tr in trs:
        date = tr.select('.td-date span')[0].get_text()
        node = tr.select('td a')[0]
        title = node.get_text()
        url = DOMAIN_URL % node.attrs['href'].replace('../../', '')
        post_NO = tr.select('.td-right')[0].get_text()
        all_content.append((date, title, url, post_NO))
        # print('======', date, title, url, post_NO)


def write_excel(file_path, content):
    # write_head()
    workbook = xlwt.Workbook(encoding='utf-8')
    # style = get_style(workbook)
    worksheet = workbook.add_sheet('result')
    write_head(worksheet, ('成文日期',	'标题', 'URL', '发文字号'))
    write_row(worksheet, content)
    # worksheet.write(0, 0, 'cell contents', style)
    workbook.save(file_path + '/result.xls')

# 获得html
def get_html(url):
    header={'user-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=header)
    res.encoding = 'utf-8'
    return  BeautifulSoup(res.text, 'html.parser')


def get_all_information(page_number):
    first_page = get_first_page()
    all_content = []
    get_content(first_page, all_content)
    count = 1
    while count < page_number:
        html = get_html(BASE_URL % count)
        get_content(html, all_content)
        count += 1
    # print(all_content)
    return all_content

    # print(html)

def get_first_page():
    first_page = get_html(INIT_URL)
    # print(first_page)
    return first_page


if __name__ == '__main__':
    print('''==================================================  欢迎进入生态环境爬虫系统 =================================================''')
    print('''使用说明：\n\t\t\t\t1.请输入文件存储的盘符，默认为c盘，若为c盘，则文件最终会存储在c盘下的out_put目录下；
           \n\t\t\t\t2.请输入想要获取的文件页数；''')
    file_path = input('请输入文件所在盘：')
    if not file_path:
        file_path = 'c'
    file_path += ':/out_put'
    create_dir(file_path)
    page_number = int(input('请输入你想获得的文件页数：'))
    all_content = get_all_information(page_number)
    write_excel(file_path, all_content)