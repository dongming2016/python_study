#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/13 21:34
from collections.abc import Iterable  # 此处变成了collections.abc
print(isinstance('abc', Iterable))

for key in 'abc':
    print(key)

# 将数组转化为键值对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

d = {'a':1, 'b':2, 'c':3}
for k, v in d.items():
    print(k, v)
for v in d.values():
    print(v)

# 迭代多个变量
for v1, v2 in [(1, 2), (2, 3), (3, 4)]:
    print(v1, v2)

for v1, v2,v3 in [(1, 2, 3), (2, 3, 4), (3, 4, 5)]:
    print(v1, v2, v3)