#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/9 22:45


# 异常的处理几乎是所有语言都需要碰到的问题
# python异常处理的语句为 try  except finally
# raise为主动抛出异常的关键字
# 抛出的异常为某个异常类的实例
# 异常可以通过继承的方式扩展
# 用logging打印出堆栈信息
import logging


class IntegerError(TypeError):
    pass


def divide(input_1):
    print(type(input_1))
    if not isinstance(input_1,int):
        raise IntegerError('type of input should be integer')  # 抛出异常
    return 10 / input_1


def main():
    try:
        divide('10')
        # divide(0)
    except IntegerError as e:  # except 为捕获异常，java中用catch来捕获
        logging.exception('error input', e)
    finally:
        print('hello future!')  # finally中的代码一定会执行
    print('end')  # 这一段代码不一定执行


main()

