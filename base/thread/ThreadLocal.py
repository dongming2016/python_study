#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/21 20:39

# 多线程下多个程序使用局部变量时需要一层一层的传递，很麻烦
# 于是高级编程语言如java，python都为每个线程备份一个副本的方案，即LocalThread，每个线程的局部变量都挂在当前线程的堆栈里
# 不与其他线程共享
import threading

# 创建全局ThreadLocal对象：
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('zhangsan',))
t2 = threading.Thread(target=process_thread, args=('lisi', ))
t1.start()
t2.start()
t1.join()
t2.join()
