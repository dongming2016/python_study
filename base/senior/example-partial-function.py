'''
python偏函数
将部分参数固定
'''
import functools
functools.partial


def int2(x):
    return int(x, base=2)


def partial(*args, **kwargs):
    if len(args)<1:
        raise TypeError('the function is required!')
    f, *args = args
    if not callable(f):
        raise TypeError('the first argument should be function')

    def gen(*args1):
        return f(*args1, *args, **kwargs)
    return gen


int3 = partial(int, base=2)
print(int3('100'))
max2 = partial(max, 10)
print(max2(1, 2, 3, 4))


