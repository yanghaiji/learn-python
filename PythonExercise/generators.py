#coding:utf-8

"""
desc: 写一个生成器
author: ben
date: 2018-05-19
"""

def gen(n):
    array = []
    for item in range(n):
        array.append(item ** item)
    return array

if __name__ == "__main__":
    # for item in fib(100):
    #     print item
    for item in gen(1000):
        print item