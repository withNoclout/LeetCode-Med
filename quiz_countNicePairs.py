class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        MOD = 10**9 + 7

        def rev(x):
            return int(str(x)[::-1])

        diff = [x - rev(x) for x in nums]
        cnt = Counter(diff)
        res = 0
        for v in cnt.values():
            res = (res + v * (v - 1) // 2) % MOD
        return res
