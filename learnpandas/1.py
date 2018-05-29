#coding:utf-8

"""
desc: series对象的使用总结
author: ben
date: 2018-05-28
"""

from pandas import Series

a = Series([1, 2, 3, 4])
#Series的字符串表现形式是：索引在左边，值在右边，没有指定索引，则自动创建

#打印元素
# print a.values
# #打印索引
# print a.index
# print a

#自定义索引
b = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print b
#
# #使用索引取值
# print b['a']
#
# #数组运算
# print a[a > 2]
#
# #将Series看成一个定长有序字典
# print 'c' in b

#可以使用字典直接创建Series，因为可以将Series看成是一个定长的有序字典
c = {'a':1, 'b':2, 'c':3}
obj = Series(c)
# print obj

#可以使用Series自动对齐不同索引的数据
d = {'b':3, 'c':9, 'd':5}
obj1 = Series(d)
print obj + obj1