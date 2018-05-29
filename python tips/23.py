# coding:utf-8

"""
desc: 协程coroutines
author:ben
date: 2018-05-17
"""

# 生成器
def fib(n):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for i in fib(10):
    print i