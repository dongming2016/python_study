#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/28 0:28

class School(object):
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not isinstance(value, int):
            raise TypeError('input should be integer')
        elif value < 1 or value > 6:
            raise ValueError('input should range between 1 and 6')
        else:
            self._grade = value

    @property
    def x(self):  # readonly
        return 7 - self._grade


s = School()
s.grade = 2
print(s.grade)
# s.grade = '2'
# print(s.grade)
# s.grade = 0
# print(s.grade)
# s.x = 8
print(s.x)
