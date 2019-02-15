#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/15 0:07

from io import StringIO,BytesIO

# StringIO和BytesIO读写的都是内存中的数据，速度回快于从文件硬盘中读取的速度。
f = StringIO()
f.write('Hello\nzhong hui xiao xian nv!\n I\'m Chen Min')
print(f.getvalue())
print(f.getvalue())
# f.write('abcccccccccccccc')
# l = StringIO('12344')
# s = l.readline()
# print(s)
# while True:
# s = f.read()
# # if s == ' ':
# #     break
# print(s.strip())
