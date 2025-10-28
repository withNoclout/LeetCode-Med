class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = min_sum = res = 0
        for x in nums:
            max_sum = max(x, max_sum + x)
            min_sum = min(x, min_sum + x)
            res = max(res, abs(max_sum), abs(min_sum))
        return res
