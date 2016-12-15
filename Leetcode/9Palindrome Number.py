#coding:utf-8

#题目的意思是判断给定的一个数是不是回文数
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        flag = True
        for i in range(len(y)):
            if y[i] != y[-i-1]:
                flag = False
                break
        return flag
        