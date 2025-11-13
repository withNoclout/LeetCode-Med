from collections import deque

class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        m, n = len(grid), len(grid[0])
        lo, hi = pricing
        sr, sc = start
        if grid[sr][sc] == 0:
            return []

        dist = [[-1] * n for _ in range(m)]
        dist[sr][sc] = 0
        q = deque([(sr, sc)])
        candidates = []

        while q:
            r, c = q.popleft()
            val = grid[r][c]
            if val > 1 and lo <= val <= hi:
                candidates.append((dist[r][c], val, r, c))
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        candidates.sort()  # sorts by (distance, price, row, col)
        return [[r, c] for _, _, r, c in candidates[:k]]
