class Solution(object):
    def maximumSafenessFactor(self, grid):
        import heapq
        from collections import deque
        
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Multi-source BFS to find Manhattan distance to nearest thief
        q = deque()
        dist = [[-1] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        while q:
            r, c = q.popleft()
            d = dist[r][c]
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = d + 1
                    q.append((nr, nc))
                    
        # Dijkstra (Max-Heap) to find path with max min-safeness
        # Store (-safeness, r, c)
        pq = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while pq:
            s, r, c = heapq.heappop(pq)
            s = -s
            
            if r == n - 1 and c == n - 1:
                return s
                
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(pq, (-min(s, dist[nr][nc]), nr, nc))
                    
        return 0