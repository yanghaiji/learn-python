#coding:utf-8

"""
desc: DataFrame（表格型数据结构）对象的使用
author: ben
date: 2018-05-29
"""

from pandas import DataFrame

"""
DataFrame既有行索引也有列索引，可以看成是Series对象组成的字典，可执行面向行和面向列的操作
"""

#　构建DataFrame
## 传入一个等长列表或者字典
data = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5], 'c':[3, 4, 5, 6]}
obj = DataFrame(data)
### DataFrame自动添加索引
# print obj
## 指定列序列，是的DataFrame列按照要求排列
obj1 = DataFrame(data, columns=['c', 'b', 'a'])
# print obj1
#列不存在的话，对应的元素值为NaN
obj2 = DataFrame(data, columns=['c','b', 'a', 'd'])
print obj2