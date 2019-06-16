#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/5/31 23:30
import folium
import  time
import requests
from urllib.request import quote
import numpy as np
import pandas as pd
import seaborn as sns
import webbrowser
from folium.plugins import HeatMap
address = ['中国','日本','美国']


def getid(dizhi):
    url = "http://api.map.baidu.com/geocoder/v2/"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
    payload = {
        'output': 'json',
        'ak': 'X8zlxPUdSe2weshrZ1WqnWxb43cfBI2N'
    }
    addinfo = []
    for i in dizhi:
        payload['address'] = i
        try:
            content = requests.get(url, params=payload, headers=header).json()
            addinfo.append(content['result']['location'])
            print("正在获取{}的地址！".format(i))
        except:
            print("地址{}获取失败，请稍后重试！".format(i))
            pass
        time.sleep(.5)
    print("所有地址均已获取完毕！！！")
    return (addinfo)


if __name__ == "__main__":
    # 计时开始：
    t0 = time.time()
    myaddress = getid(address)
    print(myaddress)
    t1 = time.time()
    total = t1 - t0
    print("消耗时间：{}".format(total))