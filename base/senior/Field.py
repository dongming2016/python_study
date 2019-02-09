#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/6 13:48


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.column_type)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'varchar(100)')