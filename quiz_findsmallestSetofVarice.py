class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
        return [i for i in range(n) if indegree[i] == 0]
