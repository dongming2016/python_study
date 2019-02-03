#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 12:42

# 这份代码的优点：
# 代码思路简单，便于初学者学习
# 这一份代码一眼看去有两大不足
# 1.无注释
# 2.无异常捕获

import os  # OS routines for NT or Posix depending on what system we're on.系统相关的类，系统路径,系统环境等，os.path便是获取路径的
# import urllib2   # 用来向网站发送请求
import requests  # 可以替代urllib2
import re  # 正则表达式
from lxml import etree  # 用来处理html文档


# 将字符串保存在某个文件路径下面
# save_path是保存路径
# filename是文件名
# slist是保存的文字内容
def StringListSave(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"
    with open(path, "w+") as fp:
        for s in slist:
            fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))


# 利用正则表达式获取文档中需要的信息
# 此处需要的信息是用h2标签展示的文字和a标签标示的链接
# 命名方式不规范，一般函数小写开头
def Page_Info(myPage):
    '''Regex'''
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
    return mypage_Info

# 使用xpath，通过路径寻找html文档中的对应元素，详细的需要展开讲，此处不便备注
def New_Page_Info(new_page):
    '''Regex(slowly) or Xpath(fast)'''
    # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)\.html".*?>(.*?)</a></td>', new_page, re.S)
    # # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)">(.*?)</a></td>', new_page, re.S) # bugs
    # results = []
    # for url, item in new_page_Info:
    #     results.append((item, url+".html"))
    # return results
    dom = etree.HTML(new_page)  # 读入html文档，并生成一棵dom树
    new_items = dom.xpath('//tr/td/a/text()')  # 遍历树，找到需要的文字
    new_urls = dom.xpath('//tr/td/a/@href')  # 遍历树，找到需要的链接
    assert(len(new_items) == len(new_urls))
    return zip(new_items, new_urls)

def Spider(url):
    i = 0
    # print "downloading ", url  此处代码有问题
    print("downloading ", url)  # 打印url路径，url就是我们在浏览器的导航出看到的http://www.runoob.com/python/python-exceptions.html这种路径
    myPage = requests.get(url).content.decode("gbk")  # 设置解码格式
    # myPage = urllib2.urlopen(url).read().decode("gbk")
    myPageResults = Page_Info(myPage)  # 获取需要的文档信息
    save_path = u"网易新闻抓取"  # 保存的路径，建议用英文路径，避免后面可能出现的乱码等问题
    filename = str(i)+"_"+u"新闻排行榜"  # 保存的文档名称
    StringListSave(save_path, filename, myPageResults)  # 保存到文件中
    i += 1
    # 循环保存相关的文件信息
    # 此处与上面的代码是同构的，可以用递归来解决
    for item, url in myPageResults:
        # print "downloading ", url
        print("downloading ", url)
        new_page = requests.get(url).content.decode("gbk")
        # new_page = urllib2.urlopen(url).read().decode("gbk")
        newPageResults = New_Page_Info(new_page)
        filename = str(i)+"_"+item
        StringListSave(save_path, filename, newPageResults)
        i += 1


if __name__ == '__main__':
    print("start")  # 此处使用日志是非常正确的做法，但最好加上时间戳
    start_url = "http://news.163.com/rank/"  #  此处是网站的url
    Spider(start_url)   # 调用spider函数，开启爬虫
    print("end")