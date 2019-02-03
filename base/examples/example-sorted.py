#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/16 16:49

'''
排序函数
sorted
'''

print(sorted([{'a': 1}, {'b': -9}, {'c':2}, {'d': 0}], key=lambda x1: list(x1.values())[0], reverse=True))
# print({'a': 1}.keys().get(0))

# for a in {'a': 1}.values():
#     print(a)
# print(list({'a': 1}.values()))