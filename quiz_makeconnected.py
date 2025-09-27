class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1

        # build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return components - 1
