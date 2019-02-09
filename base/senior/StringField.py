#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/7 17:31


import Field


# print(Field)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
