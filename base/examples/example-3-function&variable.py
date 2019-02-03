'''
函数，其英文名function已经表示了其意义，函数便是实现某一功能的一段代码。
它分为函数的定义和调用。
'''


# 函数定义, def 函数名(参数1， 参数2， 参数3……)
# 函数名需做到见名知意
def m_subtract(a, b):
    return a - b  # return 是返回结果的意思


# 输入时一定要做类型检查
def m_subtract1(a, b):
    if not (isinstance(a, (int, float)) &  isinstance(b, (int, float))):
        raise TypeError('input should be integer')
    return a - b


# 数据类型检查2
def m_subtract2(a: float, b: float):
    return a - b


# python是运行时执行类型检查，而有些语言，如java是编译时类型检查
print(m_subtract2(2, 1))
# print(m_subtract2('2', '1'))
m_subtract1(1, 2)


# 调用函数
print(m_subtract(1, 2))


# 函数的返回值可为0,1,2……
def m_multi_return(a, b):
    return a,b


print(m_multi_return(1, 2))


# 参数列表长度可变的函数,
def m_sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result


print('m_sum(1, 2, 3):', m_sum(1, 2, 3))


# 定义函数时，给参数默认值,不改变该参数时，执行某些默认行为
# 必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
def m_default_value(a, is_true=True):
    if is_true:
        return a > 1
    else:
        return a <= 1
# def m_default_value2(is_true=True, a):
#     if not is_true:
#         print('hello', a)

# m_default_value2(False, 1)


print('m_default_value(1):', m_default_value(1))
print('m_default_value(1, False)：', m_default_value(1, False))


# pass的作用什么都不做
def m_void():
    pass


print(m_void())

# 使用数组作为参数默认值时可能存在的bug
# def m_f(L=[]):
#     L.append('a')
#     return L
#
#
# print(m_f())
# print(m_f())


# 关键字参数
def person(**other):
    print(other)


person(gender=1)
person(gender=2, name='lihao')


extra = {'gender':'famale', 'name':'lihao'}
person(gender=extra['gender'], name=extra['name'])
person(**extra)


# 命名关键字
def desk(*, height, width):
    print('height:', height, 'width:', width)


desk(height=1, width=2)


# 尾递归
def fact1(n):
    return recur(n, 1)


def recur(n, product):
    if n == 1:
        return n * product
    else:
        return recur(n-1, n * product)


print(fact1(100))


# 递归
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)
