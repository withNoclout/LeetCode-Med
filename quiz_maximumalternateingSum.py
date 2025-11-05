class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even, odd = 0, 0
        for x in nums:
            even, odd = max(even, odd + x), max(odd, even - x)
        return even
