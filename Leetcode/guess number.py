class Solution(object):
    def guessNumber(self, n):
        left,right = 1,n
        while left < right:
            mid = (left + right) / 2
            if guess(mid) == 1:
                left = mid +1
            else:
                right = mid
        return left

