class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        res = 0
        bitlen = 0
        for i in range(1, n + 1):
            # increase bit length when i is a power of two
            if (i & (i - 1)) == 0:
                bitlen += 1
            res = ((res << bitlen) | i) % MOD
        return res
