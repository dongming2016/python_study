#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/22 23:26


class Student(object):

    def __init__(self, name, age):
        '''
        name,age is needed
        '''
        self.name = name
        self.age = age

    def print_student(self):
        print('name: %s, age: %d' % (self.name, self.age))

    def judge(self, age1: float):
        print('%s is %f' % (self.name, age1))


a_student = Student('chen min', 12)
# a_student.judge('12')
a_student.print_student()