#Author:LI
#保存图片
import pandas as pd #pandas和numpy是数据处理软件包
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#分段绘图，例如条形统计图设置每根柱子的区间
# 先用pd.cut分段，并取出分段数值
# 通过 precision 控制小数的位数
capital_open = pd.read_csv("./金融市场开放指数.csv",engine='python')
data = capital_open
data['cut_point']=pd.cut([float(str(x).replace('(', '-').replace(')', '')) for x in data['kaopen']],##str(x).replace('(', '').replace(')'，清理数据，剔出括号
    bins=[0,0.5,1,1.5,2,2.5], # 分割点
    labels=['0-0.5','0.5-1','1-1.5','1.5-2','2-2.5'], # 区间命名
    right=True,# 区间默认是坐开右闭
    precision=1)
data['count']=[1 for i in data['kaopen']]
count1,count2,count3,count4,count5, = 0,0,0,0,0
for x in data['cut_point']:
    if x == '0-0.5':
        count1 +=1
    elif x == '0.5-1':
        count2 += 1
    elif x == '1-1.5':
        count3 += 1
    elif x == '1.5-2':
        count4 += 1
    elif x== '2-2.5':
        count5 += 1
print(count1,count2,count3,count4,count5)
# 用sns画图，可以直接汇总每个分段的数量后绘图，而不需要groupby汇总
# 相当于回到前面，用barplot绘图
# sns.barplot(x='cut_point',y='ccode', data=data, estimator=np.sum, ci=0)
# print(data)
sns.barplot(x='cut_point',y='count', data=data, estimator=np.sum, ci=0)
plt.xlabel('open')
plt.ylabel('number')
plt.title('stastic')
plt.show()