class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        prod = 1
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
