#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/16 16:08

'''
过滤器，
其返回结果与map一样都是返回一个Iterator
'''

# print(next(filter(lambda x: x%2>0, range(10))))

'''
使用filter计算质数
思路：
删除法：
2是质数，2*n(n>1)删除
3是质数， 3*n(n>1)删除
……
'''
'''
奇数序列生成器
'''
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    # print('11111')
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


next(primes())
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
