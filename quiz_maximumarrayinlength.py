class Solution(object):
    def minimumArrayLength(self, nums):
        m = min(nums)
        for x in nums:
            if x % m != 0:
                return 1
        return (nums.count(m) + 1) // 2
