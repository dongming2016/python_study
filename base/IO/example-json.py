#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/15 23:45

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('abc', 20, 100)
print(json.dumps(s, default=lambda obj:s.__dict__))
with open('abc.txt', 'w') as f:
    # 向文件中写json数据
    json.dump(s, f, default=lambda obj: s.__dict__)


def dict2student(d):
    return  Student(d['name'], d['age'], d['score'])


with open('abc.txt') as f2:
    print(json.load(f2, object_hook=dict2student))