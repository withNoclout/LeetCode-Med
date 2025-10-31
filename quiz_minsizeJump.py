class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        n = len(obstacles)
        dp = [1, 0, 1]
        for i in range(1, n):
            for j in range(3):
                if obstacles[i] == j + 1:
                    dp[j] = float('inf')
            minv = min(dp)
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[j] = min(dp[j], minv + 1)
        return min(dp)
