class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, skip = questions[i]
            next_idx = i + skip + 1
            dp[i] = max(points + (dp[next_idx] if next_idx < n else 0), dp[i + 1])
        return dp[0]
