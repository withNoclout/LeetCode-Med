class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seen = set([0])
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            if prefix - target in seen:
                res += 1
                seen = set([0])
                prefix = 0
            else:
                seen.add(prefix)

        return res
