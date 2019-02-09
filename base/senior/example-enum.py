#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/6 9:26

# emum mains enumeration,即枚举，是java、python中常用的数据类型，其用途主要是将一类离散的常数表示为实例，避免被修改
# 如星期几
from enum import Enum,unique

Color = Enum('Color', ('red', 'blue', 'green', 'orange', 'yellow', 'purple', 'cyan'))

# print(Color.__members__.items())
# 遍历枚举
for name, memeber in Color.__members__.items():
    print(name, memeber)


# unique 检查枚举值是否重复
# 枚举一般用大写来表示
@unique
class day(Enum):
    SUN = 0  # 类属性
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6


print(day.SUN.name)  # 枚举类有两个属性，分别是name和value
print(day.SUN.value)

