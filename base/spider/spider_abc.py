#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 20:04

import requests
from bs4 import BeautifulSoup
import os
import json
import re
from datetime import datetime
import math
leaf_path = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_patition = input('请输入磁盘分区位置（如c盘，输入c,默认为c盘）：')
base_path = '%s:/bank/ABC/%s' % (file_patition, leaf_path)
base_url = 'http://ewealth.abchina.com/fs'
index_url = 'http://ewealth.abchina.com/app/data/api/DataService/BoeProductV2?i=page_NO&s=15&o=0&w=%257C%257C%257C%257C%257C%257C%257C1%257C%257C0%257C%257C0'
PAGE_SIZE = 15
record_num = 0
try:
    record_num = int(input('请输入你需要获取的文件数：'))
    if record_num <= 0:
        record_num = int(input('请输入大于0的数值:'))
        print('将会获取%s个文件' % math.ceil(record_num / PAGE_SIZE) * PAGE_SIZE)
    else:
        print('将会获取%s个文件' % math.ceil(record_num / PAGE_SIZE) * PAGE_SIZE)
except:
    record_num = int(input('请输入大于0的数值:'))
    print('将会获取%s个文件' % math.ceil(record_num / PAGE_SIZE) * PAGE_SIZE)



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


# 闭包，实现计数
def count_num():
    fail_num = [0]
    def get_num():
        fail_num[0] += 1
        return fail_num[0]

    return get_num


def get_files(a_tags, ProdName,  get_all_num = None, get_success_num = None, get_fail_num = None):
    # a_tags = html.select('.main .news .list li a')
    for item in a_tags:
        href = item.get('href')
        ss = href.replace('./', '')
        href = '%s/%s' % (base_url, ss)
        html = get_html(href)
        metas = html.select('meta')
        # print(meta)
        content = ''
        for meta in metas:
            content += meta.get('content')
        result = re.findall(r'URL=\'./([a-zA-Z]\d+.pdf)\'', content)
        print('result===========================', result)
        print('getting file of %s, the (%d)th' % (result, get_all_num()))
        if result != None and len(result) > 0:
            result = result[0]
        else:
            print('can\'t get file %s' % ProdName)
            return
        print(result)
        print('%s/%s' % (base_url, result))
        print()
        req = requests.get('%s/intro_list/%s' % (base_url, result))
        print(req)
        with open(base_path + '/' + ProdName + '.pdf', 'wb') as pdf:
            pdf.write(req.content)
            success_num = get_success_num()
            try:
                print('get %s success, the (%s)th file' % (ProdName, success_num))
            except:
                print('get %s success, the (%s)th file' % (ss, success_num))


def get_next_url(html):
    return html.select('.turn_page .turn_next')


def get_current_page(rows,get_all_num, get_success_num, get_fail_num):
    for row in rows:
        # print(row)
        print('getting file of %s' % row['ProductNo'])
        get_product(row['ProductNo'], row['ProdName'], get_all_num, get_success_num, get_fail_num)


def get_product(ProductNo='', ProdName='',  get_all_num = None, get_success_num = None, get_fail_num = None):
    html = get_html('%s/%s.htm' % (base_url, ProductNo))
    trs = html.select('.list_cp tr a')
    print('trs================', trs)
    get_files(trs, ProdName, get_all_num, get_success_num, get_fail_num)


def get_total_page_num(total_record_num, page_size):
    return total_record_num // page_size + 1
    # return html.select('.turn_page p span')[0].get_text()


def get_all_files(url, record_num):
    print('===========================getting files============================')
    html = get_html(url)
    # print(html.encode('utf8'))
    table_data = json.loads(str(html))['Data']
    # print(table_data['Data']['Table'])
    # rows = table_data['Data']['Table']
    page_num = math.ceil(record_num / PAGE_SIZE)

    page_num1 = get_total_page_num(int(table_data['Table1'][0]['total']), PAGE_SIZE)
    if page_num > page_num1:
        page_num = page_num1
    print('--------------------------------------------%s files will be got--------------------------------------------',
          page_num * PAGE_SIZE)
    get_fail_num = count_num()
    get_success_num = count_num()
    get_all_num = count_num()
    for page in range(page_num):
        print(index_url.replace('page_NO', str(page + 1)))
        html = get_html(index_url.replace('page_NO', str(page + 1)))
        table_data = json.loads(str(html))['Data']
        rows = table_data['Table']
        get_current_page(rows, get_all_num, get_success_num, get_fail_num)
    succes_num = get_success_num() - 1
    fail_num = get_fail_num() - 1
    all_file_num = get_all_num() - 1
    print('the number of success files: %s' % succes_num)
    print('the number of failed files: %s' % fail_num)
    print('the number of all files: %s' % all_file_num)
    print('文件被存储在     %s    目录下。' % base_path)


if __name__ == '__main__':
    get_all_files(index_url.replace('page_NO', '1'), record_num)
