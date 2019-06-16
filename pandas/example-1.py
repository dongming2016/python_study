#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/6/10 17:32

import pandas as pd
from xpinyin import Pinyin

excel = pd.read_excel('A(2009.1.1-2019.1.1).xls')
pinyin = Pinyin()
# print(excel)
# print(excel.iloc)
for loc in excel.loc[0:]:
    print(loc)