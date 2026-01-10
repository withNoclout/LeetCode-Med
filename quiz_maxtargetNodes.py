from collections import deque

class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def get_adj(edges):
            adj = {}
            for u, v in edges:
                adj.setdefault(u, []).append(v)
                adj.setdefault(v, []).append(u)
            return adj

        adj1 = get_adj(edges1)
        adj2 = get_adj(edges2)
        
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        # Helper to count nodes within 'limit' distance from 'start'
        def count_nodes(adj, start, limit):
            if limit < 0: return 0
            
            q = deque([(start, 0)])
            visited = {start}
            count = 0
            
            while q:
                node, dist = q.popleft()
                count += 1
                
                if dist < limit:
                    for neighbor in adj.get(node, []):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append((neighbor, dist + 1))
            return count

        # 1. Find the best node in Tree 2 to connect to.
        # We need a node in Tree 2 that maximizes reachable nodes within distance (k - 1).
        max_nodes_tree2 = 0
        if k > 0:
            for i in range(m):
                max_nodes_tree2 = max(max_nodes_tree2, count_nodes(adj2, i, k - 1))
        
        # 2. For each node in Tree 1, sum its internal reach and the best external reach.
        ans = []
        for i in range(n):
            # Nodes reachable in Tree 1 within distance k
            nodes_tree1 = count_nodes(adj1, i, k)
            ans.append(nodes_tree1 + max_nodes_tree2)
            
        return ans
