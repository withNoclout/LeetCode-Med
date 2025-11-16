class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0
        ans = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= total - left:
                ans += 1

        return ans
