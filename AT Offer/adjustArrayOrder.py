# coding:utf-8

# 调整数组的顺序，使得奇数均位于偶数之前，并且不改变元素之间的相对位置。

class Solution:
    def reOrderArray(self, array):
        # write code here
        result = []
        temp = []
        for item in array:
            if item % 2 != 0:
                result.append(item)
            else:
                temp.append(item)
        result = result + temp
        return result