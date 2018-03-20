# coding:utf-8

# 非递归实现斐波拉契数列

def fibonacci(n):
    if n < 1:
        return 0

    result = []

    for i in range(n):
        if i < 2:
            result.append(1)
        else:
            result.append(result[-1] + result[-2])
    return result

