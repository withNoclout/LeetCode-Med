class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        best = -1
        cur = 0
        left = 0
        for right, v in enumerate(nums):
            cur += v
            while cur > target and left <= right:
                cur -= nums[left]
                left += 1
            if cur == target:
                best = max(best, right - left + 1)

        return -1 if best == -1 else n - best
