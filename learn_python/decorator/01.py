# coding:utf-8
"""
time: 2019-12-01
desc: 一个最简单的装饰器
"""
import time
from functools import wraps

def time_it(func):
    """
    输出函数的运行时间
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        process_time = end_time - start_time
        print(func.__name__, process_time)
        return result
    return wrapper

@time_it
def func_a():
    time.sleep(2)


if __name__ == '__main__':
    func_a()
