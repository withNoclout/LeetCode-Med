class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            gold = grid[x][y]
            grid[x][y] = 0
            best = 0
            for dx, dy in directions:
                best = max(best, dfs(x + dx, y + dy))
            grid[x][y] = gold
            return gold + best

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))
        return ans
