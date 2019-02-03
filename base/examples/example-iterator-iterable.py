#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/15 20:14

'''
1.可迭代对象 list、tuple、dict、set、str
2.迭代器
'''

from collections.abc import  Iterable,Iterator

print(isinstance([], Iterable))
print(isinstance((x for x in range(10)), Iterator))

