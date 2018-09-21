#coding:utf-8

#ndarray对象的学习

import numpy as np

#创建数组
a = np.array([1,2,3,4])
b = np.array([[1,2,3],[2,3,4]])
print a
print b
print a.shape
print b.shape
#改变b数组的shape属性
b.shape = 3,2
print b
b.shape = 1, -1
print b

#reshape方法
c = b.reshape(3,2)
print c
print b

#数组b和c共享数组存储内存区域，修改同步
b[0][1] = 100
print b
print c

#创建数组的函数
#arange函数:通过指定开始值、终值和步长来创建一维数组，数组不包括终值
e = np.arange(0,1,0.2)
print e

#linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint指定是否包括终值，缺省表示包括终值。
f = np.linspace(0,1,10)
print f

#logspace用来创建等比数列
g = np.logspace(0, 2, 20)
print g



