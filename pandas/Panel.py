#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/24 20:21
import pandas as pd


# 先用pd.cut分段，并取出分段数值
# 通过 precision 控制小数的位数
capital_open = pd.read_csv("C:/Users/lizho/Desktop/金融市场开放指数.csv",engine='python')
data = capital_open
data['cut_point']=pd.cut(data['kaopen'],###报错：不能比较浮点和字符串问题如何解决？
    bins=[0,0.5,1,1.5,2,2.5], # 分割点
    labels=['0-0.5','0.5-1','1-1.5','1.5-2','2-2.5'], # 区间命名
    right=True,# 区间默认是坐开右闭
    precision=1)
# 用sns画图，可以直接汇总每个分段的数量后绘图，而不需要groupby汇总
# 相当于回到前面，用barplot绘图
sns.barplot(x='cut_point',y='ccode', data=data, estimator=np.sum, ci=0)
plt.xlabel('金融开放度')
plt.ylabel('个数')
plt.title('金融开放度统计')
plt.show()