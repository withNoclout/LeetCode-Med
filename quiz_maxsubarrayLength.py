class Solution(object):
    def maxSubarrayLength(self, nums, k):
        count = {}
        left = res = 0
        for right, x in enumerate(nums):
            count[x] = count.get(x, 0) + 1
            while count[x] > k:
                count[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
