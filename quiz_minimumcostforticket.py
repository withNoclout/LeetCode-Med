class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = len(days)
        dp = [0] * (n + 1)
        durations = [1, 7, 30]
        for i in range(n - 1, -1, -1):
            dp[i] = float('inf')
            for d, c in zip(durations, costs):
                j = i
                while j < n and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])
        return dp[0]
