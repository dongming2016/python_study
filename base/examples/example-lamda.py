#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/16 18:02

'''
lamda表达式的好处，是不需要命名,从而不存在函数被覆盖的情形。但如果不命名便存在一个复用的问题。
'''

print(list(map(lambda x: x*x, [1, 3, 5, 7])))
