class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if k == 0:
            return 1
        if k > n - 1:
            return 0

        # Answer is C(n + k - 1, 2k) modulo MOD
        a = n + k - 1
        b = 2 * k
        num = 1
        den = 1
        for i in range(1, b + 1):
            num = (num * (a - i + 1)) % MOD
            den = (den * i) % MOD
        return (num * pow(den, MOD - 2, MOD)) % MOD
