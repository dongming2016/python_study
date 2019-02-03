#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/16 17:56

def function_gen(j):
    def square():
        return j*j  # 闭包，内部函数引用外部函数的变量或参数。
    return square

f = function_gen(10)
# print(f())

