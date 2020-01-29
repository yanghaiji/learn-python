# coding:utf-8
"""
desc: 类装饰器
time: 2020-01-29
"""

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("class decorator start")
        self._func(*args, **kwargs)
        print("class decorator end")


@Foo
def func():
    print("test123")

if __name__ == '__main__':
    func()
