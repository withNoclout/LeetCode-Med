class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        visited = [[False]*n for _ in range(m)]
        borders = []

        def dfs(x, y):
            visited[x][y] = True
            is_border = False
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] != orig:
                    is_border = True
                elif not visited[nx][ny]:
                    dfs(nx, ny)
            if is_border:
                borders.append((x, y))

        dfs(row, col)
        for x, y in borders:
            grid[x][y] = color
        return grid
