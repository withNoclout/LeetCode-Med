class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        import heapq
        MOD = 10**9 + 7

        # Build graph
        g = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        # Dijkstra from node n to get shortest distance to n
        INF = 10**18
        dist = [INF] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        # DP in order of increasing distance
        nodes = list(range(1, n + 1))
        nodes.sort(key=lambda x: dist[x])
        dp = [0] * (n + 1)
        dp[n] = 1
        for u in nodes:
            for v, _ in g[u]:
                if dist[v] > dist[u]:
                    dp[v] = (dp[v] + dp[u]) % MOD

        return dp[1] % MOD
