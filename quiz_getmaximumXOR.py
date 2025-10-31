class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        mask = (1 << maximumBit) - 1
        res = []
        xor_sum = 0
        for x in nums:
            xor_sum ^= x
            res.append(mask ^ xor_sum)
        return res[::-1]
