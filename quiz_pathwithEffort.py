import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (effort, x, y)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while pq:
            d, x, y = heapq.heappop(pq)
            if (x, y) == (m-1, n-1):
                return d
            if d > dist[x][y]:
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    w = abs(heights[nx][ny] - heights[x][y])
                    nd = max(d, w)
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heapq.heappush(pq, (nd, nx, ny))
        return 0
