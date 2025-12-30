class Solution(object):
    def valueAfterKSeconds(self, n, k):
        MOD = 10**9 + 7
        a = [1] * n
        for _ in range(k):
            for i in range(1, n):
                a[i] = (a[i] + a[i-1]) % MOD
        return a[n-1]
