class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        # diagonal directions (↘, ↙, ↖, ↗)
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        clockwise = {(1, 1): (1, -1), (1, -1): (-1, -1),
                     (-1, -1): (-1, 1), (-1, 1): (1, 1)}

        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(x, y, dx, dy, idx, turned):
            """Return length of longest valid segment starting at (x,y) with direction (dx,dy)."""
            best = 1
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and grid[nx][ny] == seq[idx % len(seq)]:
                best = max(best, 1 + dfs(nx, ny, dx, dy, idx + 1, turned))
            # try one clockwise turn if not used
            if not turned:
                tx, ty = clockwise[(dx, dy)]
                nx, ny = x + tx, y + ty
                if in_bounds(nx, ny) and grid[nx][ny] == seq[idx % len(seq)]:
                    best = max(best, 1 + dfs(nx, ny, tx, ty, idx + 1, True))
            return best

        seq = [1, 2, 0]  # repeating pattern
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        ans = max(ans, dfs(i, j, dx, dy, 1, False))
        return ans
