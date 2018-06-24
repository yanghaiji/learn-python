#!usr/bin/python
#coding:utf-8

'''
这道题的意思是这样的：给定一个数组和这个数组中的两个数之和，需要
求得的是可以得到这个和值的数组中两个元素的下标。并且得到的规定得到
的结果唯一，也就是数组中任意两个元素得到的和唯一。
'''

'''
第一个想法是将该数组转换存入字典中，排序，得到最终的结果。
'''

'''
第二个想法是将该数组复制，并将复制的数组排序，从最小的开始遍历，
用和值减去遍历到的元素，如果差值在数组中存在的话，就返回下标值
a.index("元素")
'''

#该方法当得到和的两个数大小相同时，会出现错误，故需改进。
# class Solution(object):
#     def twoSum(self, nums, target):
#         copyNums = sorted(nums)
#         for item in copyNums:
#             if target-item in nums:
#                 break
#
#         return [nums.index(item),nums.index(target-item)]

#改进的方法的运行时间还是相对较慢，可以使用哈希（也就是字典）进行改进。
# class Solution(object):
#     def twoSum(self, nums, target):
#         count = len(nums)
#         for i in range(count):
#             if target - nums[i] in nums[i+1:]:
#                 break
#         targetNums = nums[i+1:]
#         return [i,targetNums.index(target-nums[i])+i+2]

# class Solution(object):
#     def twoSum(selfx, nums, target):
#         count = len(nums)
#         dictArray = {}
#         for i in xrange(count):
#             if target-nums[i] in nums[i+1:]:
#                 return [i,dictArray[target - nums[i]]]

'''
想到含有数组的元素和下标，当然是转换为字典更方便一些。而且使用字典比数组
的效率高。
'''

class Solution:
    def twoSum(self, nums, target):
        dictArray = {}
        for index in xrange(len(nums)):
            if target-nums[index] in dictArray:
                return [dictArray[target-nums[index]],index]
            print "NIodhnweifh"
            dictArray[nums[index]]=index

