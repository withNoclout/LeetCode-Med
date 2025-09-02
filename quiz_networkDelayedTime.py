
import heapq 
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n+ 1  ) ] 

        for u , v, w in times : 
            graph[u].append((v,w ) ) 

        dist = [ float('inf') ] * ( n + 1 ) 
        dist[k] = 0 
        pq = [( 0 , k ) ] 

        while pq : 
            d , u = heapq.heappop(pq) 
            if d > dist[u] : 
                continue 
            for v , w in graph[u] : 
                if dist[u] + w < dist[v] : 
                    dist[v] = dist[u] + w 
                    heapq.heappush(pq , (dist[v] , v)) 

        max_dist = max(dist[1:]) 
        return max_dist if max_dist < float('inf') else -1  
