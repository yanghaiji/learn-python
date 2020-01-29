# coding:utf-8
"""
desc: 闭包
time：2020-01-28
"""

def func():
    """
    计算移动平均值（不断增加的序列值的均值）
    :return:
    """
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

if __name__ == '__main__':
    avg = func()
    print(avg(8))
    print(avg(10))
    print(avg(12))
