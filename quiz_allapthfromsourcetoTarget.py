class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        target = n - 1
        res = []
        path = [0]

        def dfs(u):
            if u == target:
                res.append(list(path))
                return
            for v in graph[u]:
                path.append(v)
                dfs(v)
                path.pop()

        dfs(0)
        return res
