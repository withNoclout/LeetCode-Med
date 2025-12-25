class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
import sys
sys.setrecursionlimit(2000)

class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        res = [0] * n
        
        def dfs(u, p, dist):
            cnt = 1 if dist % signalSpeed == 0 else 0
            for v, w in adj[u]:
                if v != p:
                    cnt += dfs(v, u, dist + w)
            return cnt

        for i in range(n):
            prefix = 0
            for v, w in adj[i]:
                count = dfs(v, i, w)
                res[i] += prefix * count
                prefix += count
                
        return res        
