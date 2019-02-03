#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/29 22:18

# 类型判断
# type
print(type('a'))
print(type('a') == str)
print(type('a') == object)

# isinstance
print(isinstance('a', object))
print(isinstance([1, 2, 3], (tuple, list)))  # 只要是后面参数二者之一便可以
print(isinstance([1, 2, 3], (tuple, str)))

# dir函数获取所有的属性和方法
# __xxx__的属性和方法在Python中都是有特殊用途的
print(dir('abc'))


class Dog(object):
    def __init__(self):
        pass

    def __len__(self):
        return 100

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


myDog = Dog()
myDog.color = 'red'
print(myDog.color)
print(len(myDog))
print(hasattr(myDog, 'color'))
print(hasattr(myDog, 'c'))
# print(getattr(myDog, 'a'))
print(getattr(myDog, 'color'))
print(getattr(myDog, 'd', 2))  # 获取对象上的属性，如果没有则返回默认值2
print(setattr(myDog, 'b', 1))  # 在对象上设置属性
print(myDog.b)
