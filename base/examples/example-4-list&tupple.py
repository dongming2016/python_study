'''
list数组
tupple元组
'''

'''
数组定义：与强类型语言不通，python的数组中的类型可以为任意类型，因此在使用python list中的数据时一定要注意检查数据的类型
'''
a = [1, 2, 3]
b = [1, True, 's']   # 不通类型的数组
c = [1, [1, 2]]      # 数组中嵌套数组
print(a, b, c)
'''
取数组中的元素
'''
print(a[0], a[1], a[2])
print(a[-1], a[-2], a[-3])  # 反向取数组，即-1表示数组的最后一位

'''
数组运算中最容易出的问题是数组越界
假设数组a长度为3时，因下标从0开始，数组的最后一个元素的索引为2，取索引为3的元素时，便找不到元素，出现数组越界
'''
print('len(a):', len(a))  # 获取数组长度的方法
try:
    print(a[3])
except Exception:
    print(Exception)


'''
数组常用的方法：增、删、改、查、排序
'''
a.append('c')   # 末尾新增
print('a1', a)
a.insert(1, 'f')   # 插入
print('a2', a)
a.pop()  # 删除末尾的值
print('a3', a)
a.pop(2)  # 删除指定索引的值
print('a4', a)
print('a5', a)
a[1] = 4  # 改
print('a6', a)
a.sort()
print('a7', a)

'''
元组：tuple
'''
tu = (1, 2)
print('tu:', tu)
print(tu[0])  # 取元组中的数据
# tu[0] = 1  # 元组中的值不能修改
tu = ()
print(tu)
# print(tu[0])
# tu[0] = 1
tu = (1)  # 数值
print(tu)
tu = (1, )  # 元组，一个元素的元组需在后面加一个逗号
print(tu)
tu = (1, 2, [1, 2, 3])
try:
    tu[2] = 0       # 改变了第二个元素的值
except Exception:
    print(Exception)

tu[2][0] = 'c1'     # 改变的是第二个元素里面的内容的值，第二个元素本身对应的值未变。第二个元素对应的是一个地址，相当于我们的门牌号
print(tu)

