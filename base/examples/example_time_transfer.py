#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 22:06
from datetime import datetime
from datetime import time

CH_NUM = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
CH_YEA, CH_MONTH, CH_DAY, CH_HOUR, CH_MINUTE, CH_SECOND = '年','月', '日', '时', '分', '秒'

now = datetime.now()
year, month, day, hour, minute, second  = now.year, now.month, now.day, now.hour, now.minute, now.second
def trans_year(y):
    while y > 0:
     yield CH_NUM[y % 10]
     # print(y)
     y //= 10


def trans_time(t):
    if t // 10 > 0:
        if t % 10 == 0:
            if t // 10 < 2:
                return '十'
            else:
                return CH_NUM[t // 10] + '十'
        else:
            if t // 10 < 2:
                # return '十'
                return '十' + CH_NUM[t % 10]
            else:
                # return CH_NUM[t // 10] + '十'
                return CH_NUM[t // 10] + '十' + CH_NUM[t % 10]
    else:
        return CH_NUM[t]

# print(trans_time(12))

def trans_time2Chinese(time):
    y = [a for a in trans_year(time.year)]
    y.reverse()
    return ''.join(y) + CH_YEA + ' ' + trans_time(time.month) + CH_MONTH  + ' '+ trans_time(time.day) + CH_DAY + ' ' \
        + trans_time(time.hour) + CH_HOUR + trans_time(time.minute) + CH_MINUTE + trans_time(time.second) + CH_SECOND


print(datetime.replace(datetime.now(), 2018, 1, 1, 0, 0, 0))
print(trans_time2Chinese(datetime.replace(datetime.now(), 2018, 1, 1, 0, 0, 0)))
print(trans_time2Chinese(datetime.replace(datetime.now(), 2018, 1, 1, 5, 10, 10)))
print(trans_time2Chinese(datetime.replace(datetime.now(), 2018, 1, 1, 5, 20, 0)))
print(trans_time2Chinese(datetime.replace(datetime.now(), 2019, 3, 15, 5, 20, 0)))
print(trans_time2Chinese(datetime.replace(datetime.now(), 2019, 10, 25, 11, 20, 0)))
print(trans_time2Chinese(datetime.replace(datetime.now(), 2019, 11, 29, 23, 20, 0)))
print(trans_time2Chinese(datetime.replace(datetime.now(), 2019, 12, 30, 23, 59, 59)))
print(trans_time2Chinese(datetime.now()))
# print(datetime.now().second//10)


