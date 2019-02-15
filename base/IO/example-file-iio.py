#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/14 23:47


# 文件读写，分为异步读写和同步读写。异步读写便是读写任务与其他任务可以同时执行，读写完成后通知主程序再执行需要依赖读写内
# 的代码，同步则是所有的代码都需要等待读写任务的完成。深入理解异步和同步读写需要理解多线程

with open('lzh', 'w') as f:
    f.write('hello, zhonghui!')

# 'w'为覆盖模式
with open('lzh', 'w') as f:
    f.write('hello, lizhonghui!')

# 'a'为追加模式，即append
with open('lzh', 'a') as f:
    f.write('hhhhhhh,zhonghui!')


# read可以指定读入字节多少
with open('lzh') as f:
    str = f.read(1000)  # 1000表示1000个字节，如果一下子读入的字节过多，可能会出现内存溢出；但每次读入的过少，则cpu会被占用的时间过长，导致程序效率低下。
    print(str)
'''
with语句相当于
try:
    f = open()
    f.read()
except IOError:
    ...
finally:
    f.close()
'''
