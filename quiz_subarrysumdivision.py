class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        res = s = 0
        for num in nums:
            s = (s + num) % k
            res += count[s]
            count[s] += 1
        return res
