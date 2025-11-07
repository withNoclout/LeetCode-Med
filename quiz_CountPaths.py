import heapq

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        g = [[] for _ in range(n)]
        for u, v, w in roads:
            g[u].append((v, w))
            g[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (distance, node)
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(pq, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD
