class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]
        for x, y in walls:
            grid[x][y] = -1
        for x, y in guards:
            grid[x][y] = 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in guards:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1 and grid[nx][ny] != 1:
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = 2
                    nx += dx
                    ny += dy

        return sum(cell == 0 for row in grid for cell in row)
