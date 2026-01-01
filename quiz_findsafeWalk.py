from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        
        # Cost to enter the starting cell
        start_cost = grid[0][0]
        dist[0][0] = start_cost
        
        # Deque for 0-1 BFS
        dq = deque([(0, 0)])
        
        while dq:
            r, c = dq.popleft()
            d = dist[r][c]
            
            # If cost equals or exceeds health, we cannot survive this path
            if d >= health:
                continue
                
            if r == m - 1 and c == n - 1:
                return True
            
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < m and 0 <= nc < n:
                    new_d = d + grid[nr][nc]
                    if new_d < dist[nr][nc]:
                        dist[nr][nc] = new_d
                        # 0-1 BFS: push front if weight 0, push back if weight 1
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
                            
        return False
