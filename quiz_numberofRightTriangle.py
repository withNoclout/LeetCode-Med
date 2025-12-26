class Solution(object):
    def numberOfRightTriangles(self, grid):
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]
        
        res = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    res += (rows[r] - 1) * (cols[c] - 1)
        return res
