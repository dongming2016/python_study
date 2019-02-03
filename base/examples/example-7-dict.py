#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/11 15:19

'''
字典和集合
dict和set

'''

# dict的定义
d={'a': 1, 'b': 2, 2: 3}
c={0: 'a', 1: 'b', 2: 'c'}
print(d)
print(c)
print('d[\'a\']', d['a'])  # 取数据
print('c[0]', c[0])  # 取数据
print('c.values()', c.values())
print('c.keys()', c.keys())
print('c.items()', c.items())
print('d.get(\'a\')', d.get('a'))
print('d.get(\'m\')', d.get('m'))  # 取数据，没有则返回None
print('d.get(\'n\', 0)', d.get('n', 0))  # 取数据，没有获取到便赋予默认值0
d['l'] = 1  # 增
print(d)
d.pop(2)  # 删
print(d)
d['a'] = 'f'  # 改
print('d[\'a\']', d['a'])
print('a' in d)  # 查看键是否在d中，在返回True，不在返回False
print('g' in d)

'''
set便是我们常说的集合
集合的特点是无序，不重复
'''
s = set([1, 3, 4])
print(s)
s1 = set([1, 2, 1, 3, 5])  # 重复了，会自动去重
print(s1)

s.add('m')  # 增
print(s)
s.pop()  # 删末尾元素
print(s)
s1.remove(1)  # 删指定index的元素
print(s1)
'''
集合运算
'''
'''
求并集
'''
n = set(['a', 'b', 1])
m = set(['f', 'b', 2])
print(m | n)
print(m.union(n))
'''
求交集
'''
print(m & n)
print(m.intersection(n))
'''
求差集
'''
print(m - n)
print(m.difference(n))
