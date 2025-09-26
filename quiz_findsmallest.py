import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def compute_sum(divisor):
            return sum((num + divisor - 1) // divisor for num in nums)

        left, right = 1, max(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if compute_sum(mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
