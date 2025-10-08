class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        neg = 0
        res = 0

        for num in nums:
            if num == 0:
                pos = neg = 0
            elif num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            else:  # num < 0
                pos, neg = (neg + 1 if neg > 0 else 0), pos + 1
            res = max(res, pos)
        return res
