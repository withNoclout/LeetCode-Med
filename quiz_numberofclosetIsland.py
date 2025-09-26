class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False  # touches boundary
            if grid[x][y] == 1:
                return True
            grid[x][y] = 1
            up = dfs(x - 1, y)
            down = dfs(x + 1, y)
            left = dfs(x, y - 1)
            right = dfs(x, y + 1)
            return up and down and left and right

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        ans += 1
        return ans
