class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        odd = even = 0
        prefix = 0
        res = 0

        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                res = (res + odd) % mod
                even += 1
            else:
                res = (res + even + 1) % mod
                odd += 1

        return res
