class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        players = sorted(zip(ages, scores))  # sort by age asc, score asc
        n = len(players)
        dp = [0] * n
        ans = 0
        for i in range(n):
            _, s_i = players[i]
            dp[i] = s_i
            for j in range(i):
                _, s_j = players[j]
                if s_j <= s_i:
                    dp[i] = max(dp[i], dp[j] + s_i)
            ans = max(ans, dp[i])
        return ans
