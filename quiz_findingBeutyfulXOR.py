class Solution(object):
    def xorBeauty(self, nums):
        res = 0
        for x in nums:
            res ^= x
        return res
