class Solution(object):
    def totalHammingDistance(self, nums):
        res = 0
        n = len(nums)
        
        for bit in range(32):  # integers up to 2^31
            ones = sum((num >> bit) & 1 for num in nums)
            zeros = n - ones
            res += ones * zeros
        
        return res

