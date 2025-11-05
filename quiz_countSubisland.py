class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid2[x][y] == 0:
                return True
            grid2[x][y] = 0
            res = grid1[x][y] == 1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                res = dfs(x + dx, y + dy) and res
            return res

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    count += 1
        return count
