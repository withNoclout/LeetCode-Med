class Solution(object):
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return True
            if r >= m or c >= n or grid[r][c] == 0:
                return False
            
            grid[r][c] = 0
            return dfs(r + 1, c) or dfs(r, c + 1)
            
        if not dfs(0, 0):
            return True
            
        grid[0][0] = 1
        return not dfs(0, 0)
