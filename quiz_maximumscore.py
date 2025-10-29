class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        nums = sorted([a, b, c])
        if nums[0] + nums[1] <= nums[2]:
            return nums[0] + nums[1]
        return (a + b + c) // 2
