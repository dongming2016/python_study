#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/6/13 14:44
import pandas as pd
import numpy as np

def create_object():
    ## 创建一个一维数组
    s = pd.Series([1, 4 ,5 ,np.nan, 6, 8 ])
    print(s)
    # 创建连续的时间列表，20180601,20180602,20180603……
    dates = pd.date_range('20180601', periods=6)
    print(dates)
    # 创建一个6*4的矩阵，矩阵的索引为上述时间，列头为ABCD
    # np.random.randn返回的是一个n*m的小数的矩阵
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    # 通过dict来创建DataFrame对象
    # 自动补齐
    df2 = pd.DataFrame({
        'A': 1.,
        'B': pd.Timestamp('20180602'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(['test', 'train', 'test', 'train'])
    })
    print(df2)
    print(df2.dtypes)
    return df, df2, dates

def view_data(df):
    # 获取DataFrame的前4行
    print(df.head(4))
    # 虎丘DataFrame的后3行
    print(df.tail(3))
    # 获取DataFrame的索引
    print(df.index)
    # 获取DataFrame的列头
    print(df.columns)

    # 将DataFrame转化为numpy数组，numpy数组都是同一类型的，但是DataFrame的每一列可以有一种数据类型
    print('=====================================================')
    print(df.to_numpy())

    # 查看数据的基本统计信息,针对浮点数据
    print(df.describe())

    # 转置
    print('========================================转置===========================')
    print(df.T)

    # 根据坐标排序,axis=0表示根据index排序，axis=1表示根据colums排序
    print(df.sort_index(axis=0, ascending=False))

    print('##############根据某一列的值排序===============================')
    print(df.sort_values(by='B', ascending=False))


def view_df2(df2):
    print(df2.to_numpy())
    print(df2.describe())

def select_data(df):
    # 选择列
    print('================================选择第1列===========================')
    print(df['A'])
    # 选择行
    print('===================================选择0至3行=======================')
    print(df[0 : 3])
    print(df['20180601': '20180603'])

def select_data2(df,dates):
    print('=================================利用标签获取横截面数据,loc的第一个参数是index，第二个是columns======================')
    print(df.loc[dates[0]])
    print('===========================利用标签获取子矩阵数据,A,B两列数据======================')
    print(df.loc[:, ['A', 'B']])
    print('===========================利用标签获取子矩阵数据,A,B两列的第一行第二行数据,使用loc时需要使用index作为参数======================')
    print(df.loc['20180601':'20180602', ['A', 'B']])
    print('==========================获取单个数据=================================')
    print(df.at[dates[0], 'A'])


def select_data3(df):
    print('======================================iloc根据position获取子矩阵,实际上与列表的运算法则一致==========================')
    print(df.iloc[3])
    print(df.iloc[3:5, 0:2])
    print(df.iloc[[1,2,4], [0, 2]])
    print(df.iat[1, 1])


def select_data4(df):
    print('=================================利用逻辑表达式来筛选数据============================================')
    print(df)
    print(df[df.A > 0])
    dfA = df[df.A > 0]
    print(dfA[dfA.B > 0])
    print(df[df > 0])
    print('======================isin()获取在该行的数据,遇到重复去最后一个==================================')
    df3 = df.copy()
    df3['E'] = ['one', ' two', 'one', 'three', 'two', 'four']
    print(df3)
    print(df3[df3['E'].isin(['two', 'four'])])



def update_data(df, dates):
    print('======================创建带有命名索引的series====================')
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
    print(s1)
    print('================================更新数据==================================')
    df['F'] = s1
    print(df)
    df.at[dates[0], 'A'] = 0
    print(df)
    df.iat[0, 1] = 1
    print(df)
    print('============================将D列的数据更新为一组数值为5的数组=========================')
    df.loc[:, 'D'] = np.array([5] * len(df))
    print(df)
    df2 = df.copy()
    print('===============================将矩阵转化为负矩阵======================')
    df2[df2 > 0] = -df2
    print(df2)

def update_data1(df, dates):
    print('======================处理数据缺失===============')
    print('redindex可以增加、修改、删除索引和列')
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
    print(df1)
    print('修改第E列的第一二行的值为1')
    df1.loc[dates[0]:dates[1], 'E'] = 1
    print(df1)
    print('====================仅显示非nan的行列===============')
    print(df1.dropna())
    print('==========================处理后的df1并未改变，是一份df1的copy==================')
    print(df1)
    print('=======================将所有的nan设置为10=================')
    print(df1.fillna(value=10))
    print('=====================')
    print(df1)
    print('=====================判断元素是否为nan===================')
    print(df1.isna())


def operation(df):
    print('=================统计平均值,默认按列统计，输入1时按行统计==================')
    print(df.mean())
    print(df.mean(1))
    print('=======================向右移========================')
    s = pd.Series([1, 2, np.nan, 3, 4,5], index=pd.date_range('20180601', periods=6)).shift(3)
    print(s)
    print('==========================减法=======================')
    print(df)
    print(df.sub(s, axis='index'))
    print('=====================apply=========================')
    print(df.apply(np.cumsum)) # cumsum将数组中的元素相加
    print('=====================================求当前列的最大值与最小值的差===============================')
    print(df.apply(lambda x: x.max() - x.min()))
    print('==================直方图=======================')
    s1 = pd.Series(np.random.randint(0, 7, size=10), index=pd.date_range('20120101', periods=10))
    print(s1)
    print(s1.value_counts())
    print('==================小写转换为答谢======================')
    s2 = pd.Series(['a', 'b', 'c', 'AslfdF', np.nan])
    print(s2.str.upper())
    print('=======================合并========================')



if __name__ == '__main__':
    df, df2,dates = create_object()
    view_data(df)
    view_df2(df2)
    select_data(df)
    select_data2(df, dates)
    select_data3(df)
    select_data4(df)
    update_data(df, dates)
    update_data1(df, dates)
    operation(df)
