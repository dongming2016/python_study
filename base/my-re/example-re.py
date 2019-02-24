#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/24 19:23


# 正则表达式
import re  # 正则表达式模块


def test_time(time_str):
    '''
    正则表达式需要会在每次调用时都编译一次，如果需要重复使用的话，优化方案是预编译，使用
      re.compile(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:'  # 时
                    r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:'  # 分
                    r'((0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$)')
    :param time_str:  被检测的字符串
    :return:  返回匹配结果
    '''
    return re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:'  # 时
                    r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:'  # 分
                    r'((0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$)', time_str)  #

    # return re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:((0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$)', time_str)  # 秒


# print(test_time('09:11:10').group(2))
print(test_time('22:22:22').groups())  # 会多一个
for m in test_time('22:22:22').groups():
    print(m)


def splitStr(someStr):
    '''
    切割部分字符串，以空格，逗号，分号为切割符
    :param someStr:
    :return:
    '''
    return re.split(r'[ |,|;]', someStr)


print(splitStr('ab;m,c,12 3'))


def nonGreedy(some_str):
    '''
    一般为贪婪匹配，即会比配到当前正则所能匹配的最大限度，但加上？变为非贪婪匹配。
    :param some_str:
    :return:
    '''
    return re.match(r'^(\d+?)(0*)$', some_str)


print(nonGreedy('1212300').groups())
