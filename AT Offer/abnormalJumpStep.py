#coding:utf-8

# 变态跳台阶

def jumpFloorII(number):
    # write code here
    if number <= 1:
        return 1
    return pow(2, number-1)
