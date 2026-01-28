import heapq
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: list[list[int]]) -> int:
        # 1. Build the graph: {u: [(v, start, end)]}
        graph = defaultdict(list)
        for u, v, s, e in edges:
            graph[u].append((v, s, e))
            
        # 2. Priority Queue: (current_time, current_node)
        # Using a heap allows us to always expand the path with the minimum time
        pq = [(0, 0)]
        seen = [False] * n
        
        while pq:
            t, u = heapq.heappop(pq)
            
            # Found the destination
            if u == n - 1:
                return t
            
            if seen[u]:
                continue
            seen[u] = True
            
            # 3. Explore neighbors
            for v, s, e in graph[u]:
                # We can only take this edge if our current time is <= the end window
                if t <= e:
                    # Next time is either when the window opens (s) or now (t), plus 1
                    t2 = max(s, t) + 1
                    if not seen[v]:
                        heapq.heappush(pq, (t2, v))
                        
        return -1
