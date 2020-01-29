# coding:utf-8
"""
desc: 带参数的装饰器
time：2020-01-29
"""
import time
import signal
import functools


def func_timeout(timeout):
    """
    添加超时时间
    :param timeout:
    :return:
    """
    def decorator(func):
        def handler(signum, frame):
            raise RuntimeError("run %s timeout !" % func.__name__)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)
            func(*args, **kwargs)
            signal.alarm(0)
        return wrapper
    return decorator


@func_timeout(timeout=10)
def func():
    time.sleep(11)
    print("#" * 100)


if __name__ == '__main__':
    func()
