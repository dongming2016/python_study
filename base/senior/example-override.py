#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/1 23:41

class School(object):
    def __init__(self, school_name):
        self.school_name = school_name

    # 相当于java中的string方法被覆盖
    # java中类的string方法是继承自object的。
    # 在调用print方法时都会调用string方法。
    def __str__(self):
        return 'school object (name: %s)' % self.school_name


print(School('doukou'))