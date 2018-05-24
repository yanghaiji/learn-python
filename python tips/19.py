#coding:utf-8

"""
desc: for ... else语句的使用
author: ben
date: 2018-05-16
"""

# 正常退出
# for item in range(10):
#     print item
# else:
#     print "end"

## 不正常结束for循环
# for item in range(10):
#     print item
#     if item == 2:
#         break
# else:
#     print "end"

## else使用
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        print(n, 'is a prime number')