# coding:utf-8

# 找到数组中出现次数大于一半的元素

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        index = 0
        member = numbers[0]

        length = len(numbers)

        for i in xrange(1, length):
            if numbers[i] != member:
                index -= 1
        return index

a = Solution()
numbers = [1,2,3,4,2,2,2,2]
b = a.MoreThanHalfNum_Solution(numbers)
print b


