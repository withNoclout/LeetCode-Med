class Solution(object):
    def countSubmatrices(self, grid, k):
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                # Calculate 2D prefix sum in-place
                if i > 0: grid[i][j] += grid[i-1][j]
                if j > 0: grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0: grid[i][j] -= grid[i-1][j-1]
                
                if grid[i][j] <= k:
                    res += 1
                else:
                    # Since grid values are non-negative, the sum will only increase along the row.
                    break
                    
        return res
