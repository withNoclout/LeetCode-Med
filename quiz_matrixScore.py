class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # Flip rows to make the first column all 1s
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        # For each column, decide whether to flip to maximize number of 1s
        ans = 0
        for j in range(n):
            ones = sum(grid[i][j] for i in range(m))
            ones = max(ones, m - ones)  # flip column if better
            ans += ones * (1 << (n - 1 - j))
        return ans
