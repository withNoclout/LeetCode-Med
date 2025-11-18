class Solution(object):
    def minPathCost(self, grid, moveCost):
        m, n = len(grid), len(grid[0])
        dp = [row[:] for row in grid]   # dp[i][j] = min cost to reach cell (i,j)

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = float('inf')
                for k in range(n):
                    val = grid[i-1][k]
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[val][j] + grid[i][j])

        return min(dp[-1])
