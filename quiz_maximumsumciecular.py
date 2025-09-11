class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        cur_max = cur_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        for n in nums:
            cur_max = max(cur_max + n, n)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + n, n)
            min_sum = min(min_sum, cur_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
