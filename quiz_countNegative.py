class Solution(object):
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        r, c = m - 1, 0
        res = 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                res += n - c
                r -= 1
            else:
                c += 1
        return res
