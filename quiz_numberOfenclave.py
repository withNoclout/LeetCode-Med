class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 0
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
        
        # Remove land cells connected to the boundary
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        # Count remaining land cells
        return sum(grid[i][j] == 1 for i in range(m) for j in range(n))
