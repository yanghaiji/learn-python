class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = len(nums)
        p = 0
        for i in range(0,count):
            if nums[i] != 0:
                nums[p] = nums[i]
                p = p + 1
        for j in range(p,count):
            nums[j] = 0