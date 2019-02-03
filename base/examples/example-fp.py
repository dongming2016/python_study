#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/15 20:46
'''
        将函数当参数传入到另一个函数中
        函数和其他数据类型如数组，字符串，整型一样可以被赋值给新的变量
'''


def sum(c, d, f):
    if not isinstance(f, function):
        raise TypeError('f should be function')
    return f(c) + f(d)


print(sum(-1, 1, abs))