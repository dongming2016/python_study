#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/13 21:07
# 取list中的部分元素
'''
    返回数组的部分列表
'''
def getPartData(list1, startIndex=0, endIndex=0, step=1):
    return list1[startIndex: endIndex: step]


print(getPartData([1,2,3,4,5,6,7,8,9], 0, 4, 2))
print(getPartData([1,2,3,4,5,6,7,8,9], -1, -6, -2))
print(getPartData([1,2,3,4,5,6,7,8,9], -1, -4, -2))
print(list(range(20)))
print('abcd'[1:4])  # 前闭后开
