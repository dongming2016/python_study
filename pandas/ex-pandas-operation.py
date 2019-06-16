
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/6/16 9:34

import pandas as pd
import numpy as np

class Operation_Ex(object):
    '''
    本文为pandas的操作学习文档
    '''
    def __init__(self):
        self.s = pd.Series(pd.date_range('20190601', periods=6))
        self.data = pd.DataFrame(np.random.randn(6, 4), index=self.s, columns=list('ABCD'))
        # dataFrame的列长度需一致
        self.data1 =  pd.DataFrame({
            'A': 2,
            'B': pd.Series(1,index=list(range(5)), dtype='float32'),
            'C': np.array([3] * 5, dtype='int32'),
            'D': pd.Categorical(['cat', 'mouse', 'rabbit', 'snake', 'tiger'])
        })
        self.data2 = pd.DataFrame(np.random.randn(10, 4))
        self.data4 = pd.DataFrame({
            'A': ['foo', 'bar', 'foo', 'foo', 'bar', 'bar', 'foo', 'bar', 'foo', 'foo'],
            'B': ['1', '2', '3', '1', '2', '1', '1', '2', '3', '3'],
            'C': np.random.randn(10),
            'D': np.random.randn(10)
        })
        # print(self.s, self.data, self.data1)

    def merge_op(self):
        print('=============================================origin data=================================')
        print(self.data2)
        data2 = self.data2
        pieces = [data2[:3], data2[3:7], data2[7:]]
        print('=========================concat==============================')
        print(pieces)
        print(pd.concat(pieces))

    def join(self):
        left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': ['a', 'b']})
        right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': ['a', 'b1']})
        print('=========================merge==========================')
        print('''
        merge实际上是以某列为连接关键字，值相等时，便将两个DataFrame合并。
        其算法是，遍历left.key。left.key在right.key中遍历，找到相同的值，便将两者合并，直到right中的key遍历完。
        result = []
        i,j = 0,0
        for lk in left.key:
            for rk in right.key:
                if lk == rk:
                   result.append(left[i], right[j])
                j+=1
            i += 1
        ''')
        print(pd.merge(left, right))


    def appdend_op(self):
        print('==============================origin data==========================')
        print(self.data)
        s = self.data.iloc[2]
        print(s)
        print('================================append result========================')
        print(self.data.append(s))
        print('================================append result1========================')
        print(self.data.append(s, ignore_index=True))


    def groupby_op(self):
        data4 = self.data4
        print('==============================origin data==========================')
        print(data4)
        print('==============================group by==========================')
        print('''
            group by返回的是一个DataFrameGroupBy对象，在这个对象里记录了group的索引，以及每组group的值，可以嵌套
            如果我设计，应该是这样的一个数据结构：
            {
            index1:[]
            index2:[]
            }
        ''')
        print(data4.groupby('A'))
        print('==============================group by and sum==========================')
        print(data4.groupby('A').sum())
        print('==============================group by A,B and sum==========================')
        print(data4.groupby(['A', 'B']).sum())

    @staticmethod
    def reshape_op():
        tuples = list(zip(*[['bar', 'baz', 'baz', 'baz', 'baz', 'baz', 'zip', 'sa', 'baz1', 'dx'],
                            ['1', '2', '6', '4', '3', '5', '2', '2',  '4', '4']]))
        print('========================tupple===================')
        print(tuples)
        index = pd.MultiIndex.from_tuples(tuples, names=['first', 'sec'])
        df = pd.DataFrame(np.random.randn(10, 4), index=index, columns=list('ABCD'))
        print('===========================multiIndex======================')
        print(df)
        print(('==========================stack=============================='))
        print('stack是降维')
        stacked = df.stack()
        print(df.stack())
        print('===========================unstack============================')
        print('unstack时，不能有相同的索引.unstak是升高维度')
        print(stacked.unstack())
        print(stacked.unstack(1))
        print(stacked.unstack(0, 2))
        df2 = pd.DataFrame({
            'A': [1, 2, 3, 1, 2, 3, 1, 2],
            'B': ['foo', 'bar', 'baz', 'baz', 'bar', 'foo', 'foo', 'baz'],
            'C': ['A', 'B', 'C', 'D', 'A', 'B','A', 'B'],
            'D': np.random.randn(8),
            'E': np.random.randn(8)
        })
        print('=====================origin data=====================')
        print(df2)
        print('=======================pivot table======================')
        print('旋转成以A，B列为索引，A，B为索引名称；以C列为列，C为列的名称；D列为内容')
        print(pd.pivot_table(df2, values='D', index=['A', 'B'], columns='C'))
        print(pd.pivot_table(df2, values=['D', 'E'], index=['A', 'B'], columns='C'))


if __name__ == '__main__':
    oper = Operation_Ex()
    # oper.merge_op()
    # oper.join()
    # oper.appdend_op()
    # oper.groupby_op()
    Operation_Ex.reshape_op()
