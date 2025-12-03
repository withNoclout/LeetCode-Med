class Solution(object):
    def maxMoves(self, grid):
        m, n = len(grid), len(grid[0])
        curr = set(range(m))
        
        for j in range(n - 1):
            next_col = set()
            for i in curr:
                for k in [i-1, i, i+1]:
                    if 0 <= k < m and grid[k][j+1] > grid[i][j]:
                        next_col.add(k)
            
            if not next_col:
                return j
            curr = next_col
            
        return n - 1
