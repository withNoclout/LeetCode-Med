class Solution:
    def minCost(self, n: int, edges: list[list[int]], k: int) -> int:
        # If we already have k or fewer nodes, the cost is 0
        if n <= k:
            return 0
        
        # Parent array for Union-Find
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                # Path compression
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                return True
            return False

        # Kruskal's: Sort edges by weight (w)
        # Assuming edge format is [u, v, w]
        edges.sort(key=lambda e: e[2])
        
        components = n
        for u, v, w in edges:
            if union(u, v):
                components -= 1
            
            # Once we reach k components, the current edge weight 
            # is the minimum cost to achieve this spacing.
            if components <= k:
                return w
                
        return -1 # Or a relevant value if k components aren't possibclass Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        sr, sc = startPos
        tr, tc = homePos
        cost = 0

        # Move rows
        step = 1 if sr < tr else -1
        r = sr
        while r != tr:
            r += step
            cost += rowCosts[r]

        # Move cols
        step = 1 if sc < tc else -1
        c = sc
        while c != tc:
            c += step
            cost += colCosts[c]

        return cost
