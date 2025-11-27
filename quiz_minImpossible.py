class Solution(object):
    def minImpossibleOR(self, nums):
        nums_set = set(nums)
        res = 1
        while res in nums_set:
            res *= 2
        return res
