class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nextVisit)
        dp = [0] * n  # dp[i]: first day you visit room i for the first time

        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD

        return dp[-1]
