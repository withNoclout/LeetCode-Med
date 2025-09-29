class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        indegree = [0] * n

        # Calculate indegree for each node
        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    indegree[child] += 1
                    # if a node has more than 1 parent
                    if indegree[child] > 1:
                        return False

        # There must be exactly one root (indegree 0)
        roots = [i for i in range(n) if indegree[i] == 0]
        if len(roots) != 1:
            return False
        root = roots[0]

        # DFS to check connectivity and cycles
        visited = set()

        def dfs(node):
            if node == -1:
                return
            if node in visited:
                return
            visited.add(node)
            dfs(leftChild[node])
            dfs(rightChild[node])

        dfs(root)

        # All nodes must be visited exactly once
        return len(visited) == n
