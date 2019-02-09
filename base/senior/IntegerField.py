#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/7 17:35

import Field
# import types
# print(str)
# print(types)
print(Field)


class IntegerField(str):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'varchar(100)')
