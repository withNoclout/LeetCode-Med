class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])

        from collections import deque
        pacific = [[False]*n for _ in range(m)]
        atlantic = [[False]*n for _ in range(m)]

        def bfs(starts, visited):
            q = deque(starts)
            for x, y in starts:
                visited[x][y] = True
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

        pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atlantic_starts = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]

        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

