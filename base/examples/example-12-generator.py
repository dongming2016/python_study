#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/14 20:47

'''
迭代器
'''
# 简单的迭代器，使用()括着
g = (x*x for x in range(10))
# 使用方式
print(next(g))
# 使用for循环迭代
for n in g:
    print(n)

'''
斐波拉契数列
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # 相当于 t = a a=b b += t
        # 或(a,b)=(b, a+b)
        a, b = b, a + b
        n = n + 1
    return 'done'


'''
使用yield定义迭代器函数
'''
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 遇到yield先返回，下次next会从此处开始执行，且局部变量的值会驻存在内存中。而普通函数则不会驻存在内存中。
        # 相当于 t = a a=b b += t
        a, b = b, a + b
        n += 1
    return 'done'


def c(max):
    n1, p, a, b = 0, 1, 1, max
    while n1 <= max:
        yield p
        p = p * b // a
        # print(b, a)
        b -= 1
        a += 1
        n1 += 1


# print(next(c(6)))
# for i in c(6):
#     print('i:', i)
# 杨辉三角
def pascal_Triangle(max):
    m, a, b = 0, 1, 1
    while m < max:
        print([a for a in c(m)])
        m += 1


pascal_Triangle(10)



# print(next(fib1(6)))
# for f in fib1(6):
#     print(f)


