class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(grid)
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[0]*n for _ in range(n)]
        q = deque()

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = 1
            q.append((x, y))
            for dx, dy in dirs:
                dfs(x+dx, y+dy)

        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if grid[nx][ny] == 1:
                            return steps
                        visited[nx][ny] = 1
                        q.append((nx, ny))
            steps += 1
