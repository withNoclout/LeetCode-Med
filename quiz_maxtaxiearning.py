class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        by_end = [[] for _ in range(n + 1)]
        for s, e, tip in rides:
            by_end[e].append((s, tip))

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  # skip taking a ride ending at i
            for s, tip in by_end[i]:
                dp[i] = max(dp[i], dp[s] + (i - s) + tip)
        return dp[n]
