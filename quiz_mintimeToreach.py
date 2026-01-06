import heapq

class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        n, m = len(moveTime), len(moveTime[0])
        # dist[i][j][k] stores min time to reach (i, j) where next move cost is k+1
        # k=0 -> next move costs 1
        # k=1 -> next move costs 2
        dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0
        
        # Priority Queue: (time, r, c, next_move_cost)
        pq = [(0, 0, 0, 1)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            t, r, c, cost = heapq.heappop(pq)
            
            if r == n - 1 and c == m - 1:
                return t
            
            # Current state index for cost (1->0, 2->1)
            cost_idx = cost - 1
            if t > dist[r][c][cost_idx]:
                continue
            
            # Next move cost toggles between 1 and 2
            next_cost = 2 if cost == 1 else 1
            next_cost_idx = next_cost - 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    # Calculate arrival time at neighbor
                    # Must wait until moveTime[nr][nc]
                    new_time = max(t, moveTime[nr][nc]) + cost
                    
                    if new_time < dist[nr][nc][next_cost_idx]:
                        dist[nr][nc][next_cost_idx] = new_time
                        heapq.heappush(pq, (new_time, nr, nc, next_cost))
                        
        return -1
