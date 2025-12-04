class Solution(object):
    def differenceOfDistinctValues(self, grid):
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                tl = set()
                i, j = r - 1, c - 1
                while i >= 0 and j >= 0:
                    tl.add(grid[i][j])
                    i -= 1
                    j -= 1
                    
                br = set()
                i, j = r + 1, c + 1
                while i < m and j < n:
                    br.add(grid[i][j])
                    i += 1
                    j += 1
                    
                res[r][c] = abs(len(tl) - len(br))
        return res
