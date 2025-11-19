class Solution(object):
    def maximumXOR(self, nums):
        ans = 0
        for x in nums:
            ans |= x
        return ans
