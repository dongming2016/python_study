#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/6 13:10


def fn(self, name="wolrd"):
    print('Hello %s' %name)


# 动态创建类,运行时创建类，有时候我们需要创造动态的类型
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()

print(type(Hello))
print(type(h))

