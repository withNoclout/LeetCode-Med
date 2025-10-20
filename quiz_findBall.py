class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        res = [-1] * n

        for start in range(n):
            c = start
            for r in range(m):
                dirr = grid[r][c]
                nc = c + dirr
                # hit wall or V-shape
                if nc < 0 or nc >= n or grid[r][nc] != dirr:
                    c = -1
                    break
                c = nc
            res[start] = c
        return res
