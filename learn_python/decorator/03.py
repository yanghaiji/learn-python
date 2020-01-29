# coding:utf-8
"""
desc: 使用nonlocal方法
time：2020-01-28
"""

def func():
    """
    计算移动平均值（不保存所有历史数据）
    :return:
    """
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

if __name__ == '__main__':
    avg = func()
    print(avg(8))
    print(avg(10))
    print(avg(12))
