class Solution(object):
    def countPairs(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        comps = []

        def dfs(node):
            stack = [node]
            size = 0
            visited[node] = True
            while stack:
                u = stack.pop()
                size += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            return size

        for i in range(n):
            if not visited[i]:
                comps.append(dfs(i))

        total = n * (n - 1) // 2
        for c in comps:
            total -= c * (c - 1) // 2

        return total
