#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/4/11 21:29

import requests
from bs4 import BeautifulSoup
import os
import json
import urllib
import http
import re
from http import cookiejar

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
    # CookieJar = cookiejar.CookieJar()

    print(res.cookies.get_dict())
    auth_code = json.loads(res.content)
    # print(auth_code)
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
    print('===============================', res.cookies.get_dict())
    print(res.headers['Set-Cookie'])
    return (BeautifulSoup(res.text, 'html.parser'), res.cookies.get_dict())

def get_SYNCHRONIZER(html):
    SYNCHRONIZER_TOKEN = html.select('#SYNCHRONIZER_TOKEN')[0].get('value')
    SYNCHRONIZER_URI = html.select('#SYNCHRONIZER_URI')[0].get('value')
    # print(SYNCHRONIZER_TOKEN)
    return {'SYNCHRONIZER_TOKEN': SYNCHRONIZER_TOKEN, 'SYNCHRONIZER_URI':SYNCHRONIZER_URI }


def sign(data, cookie):
    sessions = requests.session()
    # headers = { 'Content-Length': '168', 'Content-Type': 'application/x-www-form-urlencoded',
    #            'Host': 'seat.lib.whu.edu.cn', 'Origin': 'https', 'Referer': 'https', 'Upgrade-Insecure-Requests': '1',"Content-Type": "application/x-www-form-urlencoded"
    #            ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    headers = {
        'Referer': 'https: // seat.lib.whu.edu.cn / login?username = 2018201050008',
        'Origin': 'https: // seat.lib.whu.edu.cn',
                  'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    # sessions.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    # sessions.headers['Cookie'] = 'JSESSIONID=6313FCB7670AA42FBE12AB3F768A4F98; qq%5Flogin%5Fstate=FCC6EA58C14B358628BC8E9217F996C6'
    # sessions.headers['Cookie'] = 'JSESSIONID=6313FCB7670AA42FBE12AB3F768A4F98; qq%5Flogin%5Fstate=FCC6EA58C14B358628BC8E9217F996C6'
    # sessions.max_redirects = 100
    # sessions.cookies.set('safedog-flow-item', '')
    # sessions.cookies.set('PDS_HANDLE', '21420192312461004130678185699694043')
    #
    # sessions.cookies.set('qq%5Flogin%5Fstate', 'E2223FD9C27260037B82E634FBBF5DAB')
    # sessions.cookies.set('JSESSIONID', 'C8B9FFD3D8A0CE62AB7742CF8EEB670E')
    # print(sessions)
    jar = requests.cookies.RequestsCookieJar()
    data = urllib.parse.urlencode(data).encode(encoding='utf-8')
    print(data)
    headers['JSESSIONID'] = cookie['JSESSIONID']
    jar.set('JSESSIONID',cookie['JSESSIONID'], domain='https:/seat.lib.whu.edu.cn/', path='/')
    print(jar)
    # requests.utils.
    resp = sessions.get(URL_SIGN, data=data, headers=headers, cookies=jar, allow_redirects=False)
    print(resp.headers)
    print(resp.cookies)
    resp = sessions.post(URL_SIGN, data=data, headers=headers, cookies=resp.cookies, allow_redirects=False)
    print(resp.headers)
    # res = requests.post(URL_SIGN, data=data, headers=headers, proxies={'https': 'https:202.114.65.11:443'})
    # print(resp)

def sign1(data):
    cj = http.cookiejar.LWPCookieJar()
    cookie_support = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0"}

    post_data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(URL_SIGN, post_data, headers)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')

def input_user_info():
    # user_name = input('请输入用户名：')
    user_name = '2018201050008'
    # password = input('请输入密码：')
    password = '036671'
    return (user_name, password)


if __name__ == '__main__':
    auth_id = get_auth_code(URL_AUTH_CODE)
    html, cookie = get_login_page(URL_LOGIN)
    data = get_SYNCHRONIZER(html)
    data['username'], data['password'] = input_user_info()
    data['authid'] =  auth_id

    print(data)
    print(cookie)
    # sign1(data)#
    sign(data,cookie)
