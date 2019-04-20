#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 20:04
import sys
# print(sys.path)
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import math
import sys
# sys.path.append('C:\\it\\example\\python_study')
# print(sys.path)
# C:\it\example\python_study\pdf\Pdf2xls_CMB.py
# import Pdf2xls_CMB
# from pdf import Pdf2xls_CMB
import time
# import json
import re
leaf_path = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_patition = input('请输入你想存入的磁盘分区,如c，则输入c, 默认c盘:')
if not file_patition:
    file_patition = 'c'
base_path = '%s:/bank/CMB/%s' % (file_patition, leaf_path)
print(base_path)
# out_put_path = '%s:/bank/CMB' % file_patition
base_url = 'http://www.cmbchina.com/cfweb/Personal/productdetail.aspx?code=%s&type=prodexplain'
index_url = 'http://www.cmbchina.com/cfweb/svrajax/product.ashx?op=search&type=m&pageindex=page_NO&salestatus=&baoben=&currency=&term=&keyword=&series=01&risk=&city=&date=&pagesize=20&orderby=ord1&t=0.678985470176239&citycode='
PAGE_SIZE = 20
failNum = 0
try:
    record_num = int(input('请输入你要获取的pdf数量：'))
    if record_num <= 0:
        record_num = int(input('请输入大于0的数值:'))
except:
    record_num = int(input('请输入大于0的数值:'))


def create_dir(file_path):
    if not os.path.exists(base_path):
        os.makedirs(file_path)
        return True
    else:
        print('路径已存在')
        return False


create_dir(base_path)


def get_html(url):
    header={'user-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=header)
    res.encoding = 'utf-8'
    return  BeautifulSoup(res.text, 'html.parser')


# print(soup.select('.main .news .list li a')[0].get('href'))
# soup.select('.main .news .list li a')
# failNum = 0
# 闭包，实现计数
def count_num():
    fail_num = [0]
    def get_num():
        fail_num[0] += 1
        return fail_num[0]

    return get_num


def get_files(a_tags, get_success_num, get_fail_num):
    # a_tags = html.select('.main .news .list li a')
    for item in a_tags:
        href = item.get('href')
        ss = href.replace('./', '')
        # ss.split('/')
        ProdName = item.get_text()
        if not ss.endswith('.pdf') and not ss.endswith('.doc') and not ss.endswith('.docx'):
            fail_num = get_fail_num()
            try:
                print('get %s failed, the (%s)th file' % (ProdName, fail_num))
            except:
                print('get %s failed, the (%s)th file' % (ss, fail_num))
            continue

        req = requests.get(ss)
        # print(req)
        # print(ProdName)
        try:
            with open(base_path + '/' + ProdName, 'wb') as pdf:
                pdf.write(req.content)
                success_num = get_success_num()
                try:
                    print('get %s success, the (%s)th file' % (ProdName, success_num))
                except:
                    print('get %s success, the (%s)th file' % (ss, success_num))
        except PermissionError as e:
            print(e)



def get_next_url(html):
    return html.select('.turn_page .turn_next')


def get_current_page(rows, get_all_num, get_success_num, get_fail_num, record_num):
    for row in rows:
        # print(row)
        # print_num += 1
        all_num = get_all_num()
        if all_num > record_num:
            break
        # print('getting %sth file' % all_num)
        print('getting file of %s, the (%d)th' % (row, all_num))
        get_product(row, get_success_num, get_fail_num)
        # return print_num


def get_product(ProductNo='', get_success_num=None, get_fail_num=None):
    html = get_html(base_url %  ProductNo)
    # html_str = str(html.encode('utf8'))
    # print(html_str)
    # return html
    # print(html.encode('utf8'))
    trs = html.select('#ctl00_content_panel a')
    # try:
    #     print('================', trs)
    # except UnicodeEncodeError as e:
    #     print('encoding error', e)
    get_files(trs, get_success_num, get_fail_num)


def remove_par(html):
    # print(html.encode('utf8'))
    if str(html).startswith('('):
        html = str(html).replace('(', '', 1)
    # print(html)
    if str(html).endswith(')'):
        html = html[::-1].replace(')', '', 1)[::-1]
    return html


def get_all_files(url, record_num):
    # html = get_html(url)

  # print(html)
  #   table_data = remove_par(html)
    # table_data = json.loads(html)
    # print(table_data['Data']['Table'])
    # rows = table_data['Data']['Table']
    # page_num = get_total_page_num(int(table_data['Table1'][0]['total']), PAGE_SIZE)
    # page_num = re.findall('totalRecord:(\d+),', table_data)[0]
    page_num = math.ceil(record_num / PAGE_SIZE)
    get_fail_num = count_num()
    get_success_num = count_num()
    get_all_num = count_num()
    for page in range(int(page_num)):
        # print(index_url.replace('page_NO', str(page + 1)))
        print('page NO ==========================', page + 1)
        # print_num += PAGE_SIZE
        html = get_html(index_url.replace('page_NO', str(page + 1)))
        table_data = remove_par(html)
        # table_data = json.loads(str(html))['Data']
        # print(table_data['Table'])
        result = re.findall(r'PrdCode:"(\w+)"', table_data)
        # print(result)
        get_current_page(result, get_all_num, get_success_num, get_fail_num, record_num)
    succes_num = get_success_num() - 1
    fail_num = get_fail_num() - 1
    all_file_num = get_all_num() - 1
    print('the number of success files: %s' % succes_num)
    print('the number of failed files: %s' % fail_num)
    print('the number of all files: %s' % all_file_num)
    print('文件被存储在     %s    目录下。' % base_path)


if __name__ == '__main__':
    get_all_files(index_url.replace('page_NO', '1'), record_num)
    # print(out_put_path)
    # Pdf2xls_CMB.pdf2xls(base_path, out_put_path, record_num)