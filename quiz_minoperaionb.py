from collections import Counter

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        ops = 0
        for cnt in freq.values():
            if cnt == 1:
                return -1
            ops += (cnt + 2) // 3  # minimal number of 2/3-size removals
        return ops
