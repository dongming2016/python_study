#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/16 18:20

'''
装饰器是在不改变原函数的代码的前提下，增加一些功能
常见的装饰器为日志装饰器
'''

from datetime import datetime


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): %s:' % (text, func.__name__,  datetime.now()))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('123')


now()