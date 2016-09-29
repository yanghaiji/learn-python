#coding:utf-8

'''
ransom note
该题目的意思是判断后面的字符串能否构造前面的字符串。
可以返回True，否则返回False
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        temp = True
        ranlist = list(ransomNote)
        maglist = list(magazine)
        for item in ranlist:
            if item in maglist:
                maglist.remove(item)
            else:
                temp = False
                break
        return temp

