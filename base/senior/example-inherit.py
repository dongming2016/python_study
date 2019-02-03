#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/23 23:31
# 类的继承
# 编程的第一个原则，对修改关闭，对扩展开放。开闭原则。这样做的好处是，在增加新功能时不需要修改原有代码，只需要新建文件，便于维护。


class Human(object):
    def __init__(self):
        pass

    def eat(self):
        print('human eat food')


class Child(Human):
    def eat(self):
        print('child eats cheese')


class Adult(Human):
    def eat(self):
        print('Adult eats rice')


class Animal(object):
    def eat(self):
        print('animal eats grass')


def eat_dinner(human):
    human.eat()


def eat_dinner2(human: Human):
    human.eat()


eat_dinner(Human())
eat_dinner(Child())
eat_dinner(Adult())
eat_dinner(Animal())

# 'file-like'，只要类中有相似的方法就可以调用方法
eat_dinner2(Animal())
