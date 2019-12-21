# coding:utf-8
"""
迭代器实现斐波拉契数列
"""


class Fib(object):
    def __init__(self):
        self._a = 0
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        return self._a


if __name__ == '__main__':
    for index, item in enumerate(Fib()):
        print(item)
        if index >= 9:
            break
