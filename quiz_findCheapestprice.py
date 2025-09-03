class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = 10**15
        dist = [INF] * n
        dist[src] = 0
        # up to k stops => at most k+1 edges
        for _ in range(k + 1):
            nd = dist[:]  # relax on a copy to enforce edge count limit
            for u, v, w in flights:
                if dist[u] + w < nd[v]:
                    nd[v] = dist[u] + w
            dist = nd
        return -1 if dist[dst] >= INF // 2 else dist[dst]
