#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/6 13:38
import Field
from Field import IntegerField
from Field import StringField


# 将model子类的属性存入字典中
class MetaModelClass(type):
    # 当该类作为元类传入其他类中时，会调用该方法
    # 1.当前准备创建的类的对象；
    # 2.类的名字；
    # 3.类继承的父类集合；
    # 4.类的方法集合。
    def __neg__(cls, name, bases, attrs):
        print(cls)
        if name == 'Model':
            return type.__name__(cls, name, bases, attrs)
        print('Fonnd model: %s' % name)
        mapping = dict()
        for k,v in attrs.items():
            if isinstance((v, Field)):
                print('Found mapping:%s ==> %s' % (k, v))
                mapping[k] = v
        for keys in mapping:
            attrs.pop(k)
        attrs['__mappings__'] = mapping
        attrs['table'] = name
        # print(attrs)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=MetaModelClass):
    # def __init__(self, **kw):
    #     pass
        # 调用父类的__init()方法
        # super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'"  % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        print(self)
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append(v.value)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    age = IntegerField('age')


user = User(id=123, name='zhonghui', age = 12)
user.save()
