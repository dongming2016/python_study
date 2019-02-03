'''
数据类型：
python的数据类型是弱类型的
分别是：
整型
浮点型
字符串 用单引号或双引号引着，三引号表示多行字符串
bool类型 True和False
空值 None
'''

# 整型
print(1)

# 字符串
print('1')
print('1\'')
print(r'\\')
print('''
abc
def
''')
'sss'.capitalize() #  首字母大写
print(r'''
abcs
defs
''')
# 浮点型
print(1.0)
print(1.0e1)

# byte类型
print('isinstance(b\'byte\', bytes)', isinstance(b'byte', bytes))

# 布尔值
print(True)
print(False)
print(not True)
print('1==1:',1==1)
print('not 1==1:',not 1==1)
print('1==\'1\':', 1=='1')
print('1>1：', 1>1)
print('1<1：',1<1)
print('1<=1;',1<=1)
print('1==1.0:',1==1.0)
print(1==1 and 1<1)
print(1==1 or 1<1)

# 空值
print(None)

'''
    变量，用来表示某个值的代号
        python中的变量声明特别简单，就是字母_数值，字母大小写都行
        变量声明规则，一般采用小驼峰命名法，见名知意，便于代码维护，如PI表示圆周率，height表示高度等等。
'''
name = 'liming'
print(name)
name2 = name
print(name2)
print(0o10)
print(0x10)

'''
    四则运算：
    +
    -
    *
    / 结果为浮点数
    // 结果向下取整
    % 取余
'''
print('1+1=', 1+1)
print('1-1=', 1-1)
print('1*2=', 1*2)
print('1/1=', 1/1)
print('10//3.2=', 10//3.4)
print('1.2%3.2=', 1.2%3.2)
