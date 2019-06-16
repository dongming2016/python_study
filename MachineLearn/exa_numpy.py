#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/5/25 0:46

import numpy as np
# 打印版本
print(np.__version__)
print(np.show_config())
# 创建一个长度为10的0向量
Z = np.zeros(10)
Z[4] = 1
print(Z)
#数组的内存大小
Z1 = np.zeros(10, 10)
print("%d bytes" % (Z1.size * Z1.itemsize))
# 创建一个10到49的值
Z = np.arange(10, 49)
