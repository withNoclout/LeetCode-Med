from collections import defaultdict, Counter

class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [0] * n

        def dfs(node, parent):
            count = Counter()
            count[labels[node]] += 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                count += dfs(nei, node)
            res[node] = count[labels[node]]
            return count

        dfs(0, -1)
        return res
