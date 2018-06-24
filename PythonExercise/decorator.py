#coding:utf-8
import time

# 编写执行函数
def get_time1(func):
    startTime = time.time()
    func()
    endTime = time.time()
    processTime = (endTime - startTime) * 1000
    print "The function timing is %f ms" %processTime

# 编写装饰器
def get_time2(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        processTime = (endTime - startTime) * 1000
        print "The function timing is %f ms" %processTime
    return wrapper
@ get_time2
def myfunc1():
    print "start func"
    time.sleep(0.8)
    print "end func"

# get_time(myfunc)
# myfunc()

# print "myfunc is:", myfunc.__name__
# myfunc = get_time(myfunc)
# print "myfunc is: ", myfunc.__name__
# myfunc()

#被装饰的函数带参数
def get_time3(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        processTime = (endTime - startTime) * 1000
        print "The function timing is %f ms" %processTime
    return wrapper
@ get_time3
def myfunc2(a):
    print "start func"
    print a
    time.sleep(0.8)
    print "end func"

a = "test"
myfunc2(a)

