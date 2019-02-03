#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/31 21:41

import requests
import json
import time
import os
import re
from bs4 import BeautifulSoup as bs


def create_dir(path):
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path, '创建成功')
    else:
        print('该文件夹已存在')


# 处理页面信息
# 写作函数是代码结构清晰
# 后面代码
def handle_page_info(url, content, file_name='default.txt'):
    create_dir('url-file')
    print('url', url, 'file_name', file_name)
    with open('url-file/' + file_name, 'a',encoding='utf-8') as f:
        f.write(content+ ': ' + url + '\n\r')


def get_charset(text):
    # res = requests.get('http://corp.sina.com.cn/chn/copyright.html')
    # print(re.findall(r'charset=(\w+)', res.text))
    charsets = re.findall(r'charset=(\w+)', text)
    print(charsets)
    if not charsets or len(charsets) < 1:
        return 'utf-8'
    else:
        return charsets[0]
    # text.select('meta')
# get_charset('')


# 判断url是否合法，如果url为空或不是以http或https开头则不合法
def valid_url(url):
    return not (not url) and not (not re.match(r'http[s]*://', url))
# print(valid_url('http://news.sina.com.cn/china/'))


# 获取页面信息
def get_page_info(url):
    page_list = []
    try:
        res = requests.get(url)
        charset = get_charset(res.text)
        print(charset)
        res.encoding = charset
        text = bs(res.text, 'html.parser')
        for url1 in text.select('a'):
            print(url1.get('href'))
            # print(handle_page_info())
            url2 = url1.get('href')
            text = url1.get_text()

            if url2 == url:
                pass
            elif valid_url(url2):
                if text:
                    page_list.append((url2, text))
                    print(url1.get_text())
                handle_page_info(url2, url1.get_text())
            else:
                print('url is invalid', url2)
            # get_page_info(url2)
    except OSError as e:
        print('error', e)
    return page_list


# 将页面链接写入到文本中
def write_url_txt(url_list, all_url, start_text):
    for url, text in url_list:
        if url in all_url:
            print('repeat: ', url)
            pass
        else:
            all_url.append(url)
            print('start url', url)
            try:
                if url:
                    handle_page_info(url, text, start_text+ '.txt')
                else:
                    print(url)
            except FileNotFoundError as e:
                print('error:', e)
            print(str(text).replace('\n', ''))


# 判断url是否合法
# 当前只要url不是none，空字符串都可以
# 严格的判断需要使用正则表达式来判断
# 用函数的原因是代码功能会更具体，后面可以将url作为一个单独的模块重构。
def is_url_illegal(url):
    return not url


# 获取所有页面的链接，并将页面链接写入到txt文件中
def get_all_page(start_url, all_url, start_text='default'):
    # 如果start_url为none或者''
    if is_url_illegal(start_url):
        return
    url_list = get_page_info(start_url)
    if len(url_list) < 1:
        return
    print(url_list)
    write_url_txt(url_list, all_url, start_text)

    for (url, text) in url_list:
        if not valid_url(start_url):
            return
        get_all_page(url, all_url, str(text).replace('\n', ''))


get_all_page('https://news.sina.com.cn/china/', [], 'page_info_2')
