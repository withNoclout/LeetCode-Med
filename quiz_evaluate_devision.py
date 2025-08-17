from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for nei, val in graph[src]:
                if nei not in visited:
                    res = dfs(nei, dst, visited)
                    if res != -1.0:
                        return res * val
            return -1.0

        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))
        return ans
