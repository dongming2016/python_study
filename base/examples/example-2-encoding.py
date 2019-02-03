#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
编码：
ASCII码：1个字节
unicode：2个字节
UTF-8：3个字节 uniform transformation format
ASCII码转为UTF-8:1个字节
非ASCII码的unicode转化为UTF-8，如果一个字节的Unicode需要2个字节的utf-8,2个字节则需要3个字节，3个字节需要5个字节
UTF-16
中文编码方式
GB2312
GBK
'''
print('a'.encode('utf-8'))
print('a'.encode('ascii'))
print('中国'.encode('utf-8'))
# print('中国'.decode('utf-8'))
print('中国'.encode('ascii', errors='ignore'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('aa'))
print(len('中文'))
print(len('中文'.encode('utf-8')))

'''
占位符
以%开头
%d  digit %0d
%s  string
%f  float %.2f
'''
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.25))