class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        s = sum(nums)
        for i in range(len(nums) - 1, 1, -1):
            if s - nums[i] > nums[i]:
                return s
            s -= nums[i]
        return -1
