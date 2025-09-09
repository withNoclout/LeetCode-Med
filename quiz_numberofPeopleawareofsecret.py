class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        cur = 0  # number of people who can share on the current day

        for day in range(2, n + 1):
            if day - delay >= 1:
                cur = (cur + dp[day - delay]) % MOD
            if day - forget >= 1:
                cur = (cur - dp[day - forget]) % MOD
            dp[day] = cur

        ans = sum(dp[max(1, n - forget + 1): n + 1]) % MOD
        return ans
