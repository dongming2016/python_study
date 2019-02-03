#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/15 20:56
from collections.abc import Iterable, Iterator


# f为函数， l必须可迭代：
# map、reduce、filter、sorter都是将规则抽象的高阶函数
# 高阶函数，实际上是一种规则抽象
def map(f, l):
    if not callable(f):
        raise TypeError('the first input should be callable')
    if not isinstance(l, (Iterable, Iterator)):
        raise TypeError('the second input should be iterable')
    for a in l:
        yield f(a)
    # return [f(a) for a in l]

def f(x):
    return x * x


print(next(map(f, [1, 2, 3, 4, 5])))
# print(list(map(f, [1,23,34])))
# for i in map(f, [1, 2, 3, 4, 5]):
#     print(i)

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4]))
print(reduce(lambda x,y: x*y, [1]))
# print(reduce(lambda x,y,z: x*y*z, [1, 2, 3, 4,5]))


'''
reduce
'''


def reduce1(f, sequence, initial=None):
    if not callable(f):
        raise TypeError('the first input should be callable')
    if not isinstance(sequence, list):
        raise TypeError('the second input should be list')
    if initial == None:
        initial = sequence[0]
        sequence.pop(0)
    result = initial
    for i in sequence:
        # sequence.remove(0)
        result = f(result, i)
    return result

print(reduce1(lambda x,y: x*y, [2, 3, 23]))



