#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/25 0:10
from types import MethodType


class Car(object):
    pass


c = Car()


def move(self, distance):
    self.distance = distance
    print(self.distance)


c.move = MethodType(move, c)  # 将函数绑定在实例上
c.move(10)

# c2 = Car()
# c2.move()


def move2(self, distance):
    self.distance = distance
    print('I move %s' % self.distance)


Car.move = move2  # 将方法绑定在类上
c3 = Car()
c3.move(12)


class vehicle(object):
    __slots__ = ('speed', 'color')


v = vehicle()
v.speed = 10
print(v.speed)
# v.add_speed = 1  # 如果再在v上添加speed和color之外的属性便会报错


# 但是在子类上如果不限制则可以加
class bycycle(vehicle):
    pass


b = bycycle
b.speed =2
print(b.speed)
b.add_speed = 3
print(b.add_speed)
