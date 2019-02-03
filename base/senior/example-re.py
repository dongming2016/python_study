#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/3 21:12

# 正则表达式
import re

print(re.sub(r'\d', '', 'a123b34555c45'))
print(re.sub(r'[a-d]+', '', 'ab123cd34f'))
print(re.sub('["陈”,"大"]', '', '陈敏是大叔'))
