class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        MOD = 10**9 + 7
        maxv = (1 << p) - 1              # 2^p - 1
        base = maxv - 1                  # 2^p - 2
        exp = (1 << (p - 1)) - 1         # 2^{p-1} - 1
        return (pow(base % MOD, exp, MOD) * (maxv % MOD)) % MOD
