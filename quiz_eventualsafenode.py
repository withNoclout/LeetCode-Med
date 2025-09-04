class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        color = [0] * n  # 0=unvisited, 1=visiting, 2=safe

        def dfs(u):
            if color[u] != 0:
                return color[u] == 2
            color[u] = 1
            for v in graph[u]:
                if color[v] == 1 or not dfs(v):
                    return False
            color[u] = 2
            return True

        return [i for i in range(n) if dfs(i)]
