from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        q = deque()

        # Add all land cells as starting points
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))

        if not q or len(q) == n * n:  # all water or all land
            return -1

        ans = -1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y, d = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    ans = d + 1
                    q.append((nx, ny, d + 1))
        return ans
