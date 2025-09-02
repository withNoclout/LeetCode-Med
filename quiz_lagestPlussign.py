class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        banned = {tuple(m) for m in mines}
        dp = [[0] * n for _ in range(n)]

        # left to right
        for i in range(n):
            run = 0
            for j in range(n):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = run

        # right to left
        for i in range(n):
            run = 0
            for j in range(n - 1, -1, -1):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = min(dp[i][j], run)

        ans = 0
        # top to bottom
        for j in range(n):
            run = 0
            for i in range(n):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = min(dp[i][j], run)

        # bottom to top + compute answer
        for j in range(n):
            run = 0
            for i in range(n - 1, -1, -1):
                run = 0 if (i, j) in banned else run + 1
                dp[i][j] = min(dp[i][j], run)
                if dp[i][j] > ans:
                    ans = dp[i][j]

        return ans
