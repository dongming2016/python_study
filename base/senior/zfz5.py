#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/1 17:27
# coding:utf-8
import json
import pandas as pd
# import csv
import requests
from pyquery import PyQuery as pq
from time import time


def get_html(url):
    headers = {
        'Usre-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360EE'}
    story = requests.get(url)
    story.encoding = 'utf-8'
    # print(story.content)
    return pq(story.content)


def illegal_text(text):
    return text.find('当前页面是第') > -1 or text.find('↑返回页顶↑') > -1

def get_table_data(html, all_data, key_list):
    trs = html('.historyList')('tr').items()
    # result = [[], [], [], [], [], []]
    for tr in trs:
        # za=[]
        index = 0
        while index < 6:
            # print(key_list[index])
            print(tr('td:nth-child('+ str(index + 1) +')').text())
            if illegal_text(tr('td:nth-child('+ str(index + 1) +')').text()):
                break
            all_data.get(key_list[index]).append(tr('td:nth-child('+ str(index + 1) +')').text())
            index += 1
    print('end1========================')
    # return result


def get_datas():
    base_url = "http://vip.stock.finance.sina.com.cn/q/view/vFutures_History.php?breed=NG&start=2014-00-01&end=2014-12-31&jys=NYME&pz=NG&hy=&type=global&name=%B4%F3%B6%B91109"
    all_data = {'time': [], 'spj': [], 'kpj': [], 'zgj': [], 'zdj': [], 'cjl': []}
    key_list = ['time', 'spj', 'kpj', 'zgj', 'zdj', 'cjl']
    # print(key_list[0])
    for i in range(7):
        url = base_url+ '&page='+ str(i + 1)
        print(url)
        html =get_html(url)
        get_table_data(html, all_data, key_list)

    print(all_data)
    DataFrame = pd.DataFrame(all_data)
    DataFrame.to_csv('data3.csv', encoding='gbk')
    print('end')


get_datas()
