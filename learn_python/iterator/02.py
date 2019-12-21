# coding:utf-8
"""
生成器实现斐波拉契数列
"""
from itertools import islice

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    fib_data = fib()
    print(type(fib_data))
    print(dir(fib_data))
    print(list(islice(fib_data, 0, 10)))
