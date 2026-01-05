class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums:
            if x % 2 == 0:
                ans.append(-1)
            else:
                # Find the lowest 0 bit
                # Since x is odd, bit 0 is 1. We start checking from bit 1 (value 2)
                bit = 2
                while (x & bit) > 0:
                    bit <<= 1
                
                # 'bit' is now at the position of the first 0.
                # We subtract the bit immediately to its right (bit >> 1).
                ans.append(x - (bit >> 1))
        return ans
