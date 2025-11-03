class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]

        def row_sum(r, c1, c2):
            return row_prefix[r][c2] - row_prefix[r][c1]

        def col_sum(c, r1, r2):
            return col_prefix[r2][c] - col_prefix[r1][c]

        res = 1
        for size in range(2, min(m, n) + 1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    target = row_sum(i, j, j + size)
                    ok = True
                    for r in range(i, i + size):
                        if row_sum(r, j, j + size) != target:
                            ok = False
                            break
                    for c in range(j, j + size):
                        if col_sum(c, i, i + size) != target:
                            ok = False
                            break
                    if not ok:
                        continue
                    diag1 = diag2 = 0
                    for k in range(size):
                        diag1 += grid[i + k][j + k]
                        diag2 += grid[i + k][j + size - 1 - k]
                    if diag1 == diag2 == target:
                        res = size
        return res
