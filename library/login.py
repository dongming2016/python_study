#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/4/11 21:29

import requests
from bs4 import BeautifulSoup
import os
import json
import re

URL_AUTH_CODE = 'https://seat.lib.whu.edu.cn/captcha'
URL_LOGIN = 'https://seat.lib.whu.edu.cn/login?username=%s'
URL_SIGN = 'https://seat.lib.whu.edu.cn/auth/signIn'

def get_auth_code(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=627F12F5F8EEC3D5491D1A48A86A34C5',
        'Host': 'seat.lib.whu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://seat.lib.whu.edu.cn/login?username=2018201050008',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    auth_code = json.loads(res.content)
    print(auth_code)
    return auth_code['token']

def get_login_page(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=627F12F5F8EEC3D5491D1A48A86A34C5',
        'Host': 'seat.lib.whu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://seat.lib.whu.edu.cn/login?username=2018201050008',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    print(res.content)
    return BeautifulSoup(res.text, 'html.parser')

def get_SYNCHRONIZER(html):
    SYNCHRONIZER_TOKEN = html.select('#SYNCHRONIZER_TOKEN')[0].get('value')
    SYNCHRONIZER_URI = html.select('#SYNCHRONIZER_URI')[0].get('value')
    print(SYNCHRONIZER_TOKEN)
    return {'SYNCHRONIZER_TOKEN': SYNCHRONIZER_TOKEN, 'SYNCHRONIZER_URI':SYNCHRONIZER_URI }


def sign(data):
    sessions = requests.session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Length': '168', 'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': 'JSESSIONID=627F12F5F8EEC3D5491D1A48A86A34C5', 'Host': 'seat.lib.whu.edu.cn', 'Origin': 'https', 'Referer': 'https', 'Upgrade-Insecure-Requests': '1'
               ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    # sessions.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    # sessions.headers['Cookie'] = 'JSESSIONID=6313FCB7670AA42FBE12AB3F768A4F98; qq%5Flogin%5Fstate=FCC6EA58C14B358628BC8E9217F996C6'
    # sessions.headers['Cookie'] = 'JSESSIONID=6313FCB7670AA42FBE12AB3F768A4F98; qq%5Flogin%5Fstate=FCC6EA58C14B358628BC8E9217F996C6'
    sessions.max_redirects = 100
    resp = sessions.post(URL_SIGN, data=data, headers=headers)
    print(resp.headers)
    # res = requests.post(URL_SIGN, data=data, headers=headers, proxies={'https': 'https:202.114.65.11:443'})
    print(resp)


def input_user_info():
    # user_name = input('请输入用户名：')
    user_name = '2018201050008'
    # password = input('请输入密码：')
    password = '036671'
    return (user_name, password)


if __name__ == '__main__':
    auth_id = get_auth_code(URL_AUTH_CODE)
    html = get_login_page(URL_LOGIN)
    data = get_SYNCHRONIZER(html)
    data['username'], data['password'] = input_user_info()
    data['authid'] =  auth_id

    print(data)
    sign(data)
