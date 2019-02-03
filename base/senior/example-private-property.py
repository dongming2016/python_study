#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/23 23:12

class Student(object):
    def __init__(self, name, age: float):
        self.__name = name
        self.__age = age  # 私有变量

    def print_self(self):
        print('my name is %s, my age is %d' % (self.__name, self.__age))

    def get_name(self):
        return self.__name

    def __set_name__(self, owner, name):
        self.__name = name


s = Student('age', 12)
s.print_self()
s.__set_name__(s, '12')
s.print_self()
print(s.get_name())
