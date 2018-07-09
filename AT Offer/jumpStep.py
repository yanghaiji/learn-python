# coding:utf-8

#跳台阶问题

class Solution:
    def jumpFloor(self, number):
        # write code here

        if number <= 2:
            return number
        result = 0
        pre_first = 1
        pre_second = 2

        while number > 2:
            result = pre_first + pre_second
            pre_first = pre_second
            pre_second = result
            number -= 1
        return result