class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        # directions (↗, ↘, ↙, ↖) same order as C++
        dr = [-1, 1, 1, -1]
        dc = [1, 1, -1, -1]

        def inBounds(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c, dir, canChange, length, searchFor):
            maxi = length

            # Continue in current direction
            if dir != -1:
                nr, nc = r + dr[dir], c + dc[dir]
                if inBounds(nr, nc) and grid[nr][nc] == searchFor:
                    nextVal = 0 if searchFor == 2 else 2
                    maxi = max(maxi, dfs(nr, nc, dir, canChange, length + 1, nextVal))

            # Try a clockwise turn if allowed
            if dir != -1 and canChange:
                ndir = (dir + 1) % 4
                nr, nc = r + dr[ndir], c + dc[ndir]
                if inBounds(nr, nc) and grid[nr][nc] == searchFor:
                    nextVal = 0 if searchFor == 2 else 2
                    maxi = max(maxi, dfs(nr, nc, ndir, False, length + 1, nextVal))

            # Starting point: try all 4 directions
            if dir == -1:
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if inBounds(nr, nc) and grid[nr][nc] == searchFor:
                        nextVal = 0 if searchFor == 2 else 2
                        maxi = max(maxi, dfs(nr, nc, i, canChange, length + 1, nextVal))

            return maxi

        maxi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # start only from 1
                    maxi = max(maxi, dfs(i, j, -1, True, 1, 2))
        return maxi
