# coding:utf-8

"""
desc: 实例说明*args和**kwargs的区别
time: 2018/05/06
author: ben
"""

#函数定义
def test_args(arg, *args):
    print "the first arg is:", arg
    print "the *args is/are:", args
    print "The type of *args is:", type(args)

def test_kwargs(**kwargs):
    print "The **kwargs is: ", kwargs
    print "The type of **kwargs is: ", type(kwargs)

#函数调用
def test_args_call(arg1, arg2, arg3):
    print arg1, arg2, arg3

def test_kwargs_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

if __name__ == "__main__":
    test_args(1, 2, 3)

    test_kwargs(a=1,b=2)

    args = (1, 2, 3)
    test_args_call(*args)

    kwargs = {"arg1":1, "arg2":2, "arg3":3}
    test_kwargs_call(**kwargs)