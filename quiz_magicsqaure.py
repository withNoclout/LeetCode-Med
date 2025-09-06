class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        def is_magic(r, c):
            # center must be 5 in any 3x3 1..9 Lo Shu magic square
            if grid[r+1][c+1] != 5:
                return False

            seen = [0] * 10
            for i in range(3):
                for j in range(3):
                    v = grid[r+i][c+j]
                    if v < 1 or v > 9 or seen[v]:
                        return False
                    seen[v] = 1

            # rows and cols sum to 15
            for i in range(3):
                if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != 15:
                    return False
                if grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != 15:
                    return False

            # diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False
            return True

        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(i, j):
                    ans += 1
        return ans
