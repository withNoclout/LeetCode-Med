class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def power(a, b):
            if b == 0:
                return 1
            half = power(a, b // 2)
            res = (half * half) % MOD
            if b % 2:
                res = (res * a) % MOD
            return res

        even_count = (n + 1) // 2
        odd_count = n // 2
        return (power(5, even_count) * power(4, odd_count)) % MOD
