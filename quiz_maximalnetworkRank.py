class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        deg = [0]*n
        adj = [set() for _ in range(n)]
        for a,b in roads:
            deg[a]+=1
            deg[b]+=1
            adj[a].add(b)
            adj[b].add(a)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = deg[i] + deg[j] - (1 if j in adj[i] else 0)
                if rank > ans:
                    ans = rank
        return ans
