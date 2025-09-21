class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        hor = [[0] * (n + 1) for _ in range(m + 1)]
        ver = [[0] * (n + 1) for _ in range(m + 1)]

        # precompute continuous 1's horizontally and vertically
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i + 1][j + 1] = hor[i + 1][j] + 1
                    ver[i + 1][j + 1] = ver[i][j + 1] + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                # try largest possible side length at (i,j) as bottom-right corner
                small = min(hor[i + 1][j + 1], ver[i + 1][j + 1])
                while small > ans:
                    if hor[i + 1 - small + 1][j + 1] >= small and ver[i + 1][j + 1 - small + 1] >= small:
                        ans = small
                    small -= 1
        return ans * ans
