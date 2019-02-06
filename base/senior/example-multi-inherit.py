#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/3 22:48
# 多继承，python中的多继承是指一个子类可以继承多个直接父类


class School(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


# mixin，混入，为某个子类增加额外的功能，与java的接口有一定的相似处，但是功能是已经被实现，而接口未被实现
# 混入是将某一类公共的功能提取出来，并用来增强子类功能的类
class StudyMixin(object):
    def study(self):
        return 'I\'m studying in %s' % self._name


class PrimarySchool(School, StudyMixin):
    pass


s = PrimarySchool('abc')
print(s.study())
