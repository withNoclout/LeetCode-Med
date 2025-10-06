class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % mod

        res = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow2[right - left]) % mod
                left += 1
            else:
                right -= 1
        return res
