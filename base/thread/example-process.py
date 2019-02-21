#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/16 21:54


# 进程
import os

# getpid获取的是当前进程的id
print('Process (%s) start...' % os.getpid())

# only works on Unix/Linux/Mac:, on windows it will lead to error
# fork，将当前进程copy一份，并生成一个子进程
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is (%s)' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s)' % (os.getpid(), pid))
