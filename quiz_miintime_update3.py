import sys

# Increase recursion depth for deep DSU operations if necessary
sys.setrecursionlimit(200000)

class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def minTime(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Standard Disjoint Set Union (DSU) implementation
        parent = list(range(n))
        self.components = n

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                self.components -= 1
                return True
            return False

        # 1. Sort edges by time (weight) in ascending order.
        # edges[i] = [u, v, time]
        edges.sort(key=lambda x: x[2])

        # 2. Iterate edges from largest time to smallest.
        # We assume initially t = infinity (no edges kept, n components).
        # We gradually decrease t, which means we 'keep' edges with larger weights.
        for i in range(len(edges) - 1, -1, -1):
            u, v, t = edges[i]
            
            # Merge the nodes connected by this edge
            union(u, v)
            
            # If the number of components drops below k, we have "over-connected" the graph.
            # To maintain >= k components, we must NOT include this edge.
            # Therefore, we must remove all edges with weight <= t.
            if self.components < k:
                return t
                
        # If we can keep all edges and still have >= k components, no removal is needed.
        return 0
