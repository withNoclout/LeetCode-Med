class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        rows = {}
        for r in grid:
            t = tuple(r)
            rows[t] = rows.get(t, 0) + 1

        ans = 0
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            t = tuple(col)
            ans += rows.get(t, 0)

        return ans
