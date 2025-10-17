from collections import defaultdict

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        need = defaultdict(int)
        ops = 0
        for x in nums:
            y = k - x
            if need[y] > 0:
                need[y] -= 1
                ops += 1
            else:
                need[x] += 1
        return ops
