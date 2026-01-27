import heapq

class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Build the graph
        # For each given edge [u, v, w]:
        # 1. Normal traversal: u -> v with cost w
        # 2. Reverse traversal: v -> u with cost 2 * w
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))
            
        # Standard Dijkstra's Algorithm
        # dist[i] stores the minimum cost to reach node i
        dist = [float('inf')] * n
        dist[0] = 0
        
        # Priority Queue: (current_cost, node)
        pq = [(0, 0)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            # If we reached the target, return the cost
            if u == n - 1:
                return d
            
            # If current path is worse than what we already found, skip
            if d > dist[u]:
                continue
            
            # Explore neighbors
            for v, w in adj[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
                    
        return -1
