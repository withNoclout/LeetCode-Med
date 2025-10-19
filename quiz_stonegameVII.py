class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stones[i]

        # dp[j] will represent the best score difference for subarray [i..j]
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # If we remove stones[i], opponent faces [i+1..j]
                score_left = (pref[j + 1] - pref[i + 1]) - dp[j]
                # If we remove stones[j], opponent faces [i..j-1]
                score_right = (pref[j] - pref[i]) - dp[j - 1]
                dp[j] = max(score_left, score_right)

        return dp[n - 1]
