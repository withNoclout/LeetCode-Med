# ...existing code...
class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # difference array to maintain current sharers for each day
        diff = [0] * (n + forget + 5)
        dp = [0] * (n + 1)  # dp[i] = number of people who learn the secret on day i

        dp[1] = 1
        # schedule dp[1] to start contributing at day 1+delay and stop at day 1+forget
        diff[1 + delay] = (diff[1 + delay] + dp[1]) % MOD
        diff[1 + forget] = (diff[1 + forget] - dp[1]) % MOD

        sharers = 0
        for day in range(2, n + 1):
            sharers = (sharers + diff[day]) % MOD
            dp[day] = sharers
            start = day + delay
            end = day + forget
            if start < len(diff):
                diff[start] = (diff[start] + dp[day]) % MOD
            if end < len(diff):
                diff[end] = (diff[end] - dp[day]) % MOD

        # people who still remember the secret on day n: sum dp[i] for i in [n-forget+1, n]
        ans = 0
        for i in range(max(1, n - forget + 1), n + 1):
            ans = (ans + dp[i]) % MOD
        return
