#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/5/24 7:11

import pandas
import numpy

# california_csv = pandas.read_csv('california_housing_train.csv')
# print(california_csv.head())
# print(california_csv.describe())
# print(california_csv.hist('housing_median_age'))
# series是列表， DataFrame是键值对或者说字典，但不同于普通列表，series中的列表元素是一个对象，series也是一个对象
# DataFrame也是一个对象
cities = pandas.Series(['San Fransisco', 'San Jose', 'Sacramento'])
population = pandas.Series([852469, 1015785, 485199])
cities_frame = pandas.DataFrame({'cities': cities, 'population': population})

# 对矩阵运算
print(population/1000)
print(numpy.log2(population))
# 函数式编程中的一种，filter
print(population.apply(lambda val: val > 100000))
cities_frame['Area square miles'] = pandas.Series([46.87, 176.53, 97.92])
# pandas重载了/符号
# 重载方式见https://hellowac.github.io/programing%20teach/2017/06/06/fluentpython13.html
cities_frame['Population density'] = cities_frame['population'] / cities_frame['Area square miles']
print(cities_frame)

# 布尔值 Series 是使用“按位”而非传统布尔值“运算符”组合的。
# 必须先计算出前一列后再计算后一列
cities_frame['is_city_san_sqr50'] = (cities_frame['Area square miles'] > 50) & (cities_frame['cities'].apply(lambda name: name.startswith('San')))
print(cities_frame )
# print(cities_frame['Area square miles'] > 50 & cities_frame['cities'].apply(lambda val: val.find('San') > -1))
print(cities_frame.index)
print(cities_frame['cities'].index)

print('+++++++++++++++++++++++++++++++++++++++++++')
print(cities_frame.reindex([2,0,1]))
print('+++++++++++++++++++++++++++++++++++++++++++')

print(cities_frame)

dates = pandas.date_range('20190101', periods=5)
df = pandas.DataFrame(numpy.random.randn(5, 4), columns=list('ABCD'), index=dates)
print(df)
print(df['B'])

######### 选择多列
print(df[['A', 'B']])

######### 交换列 方法1
df[['A', 'B']] = df[['B', 'A']]
print(df[['A', 'B']])

#### loc的第一个参数是行索引， 第二个参数是列索引
print('=================================================')
print( df.loc['20190101':'20190103 ', ['B', 'A']])
print( df.loc[:, ['B', 'A']])
print('=================================================')
print( df.loc[:, ['B', 'A']])
df.loc[:,['B', 'A']] = df[['A', 'B']]

print('=================================================')
print(df)

print('=================================================')
df.loc[:,['B', 'A']] = df[['A', 'B']].to_numpy()
print(df)


