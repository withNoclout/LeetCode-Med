class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            res = max(res, right - left)  # delete one element (at most one zero)

        return res
