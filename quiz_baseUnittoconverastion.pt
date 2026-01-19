class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def baseUnitConversions(self, conversions):
        """
        :type conversions: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        # The graph is a tree with n nodes and n-1 edges
        n = len(conversions) + 1
        
        # Build adjacency list: source -> (target, factor)
        adj = [[] for _ in range(n)]
        for src, tgt, factor in conversions:
            adj[src].append((tgt, factor))
            
        ans = [0] * n
        ans[0] = 1  # Base unit 0 is 1 unit of itself
        
        # BFS to traverse the conversion tree
        queue = [0]
        idx = 0
        
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            
            # 1 unit of u = ans[u] units of 0
            # 1 unit of u = factor units of v
            # Therefore: 1 unit of 0 = (ans[u] * factor) units of v
            for v, factor in adj[u]:
                ans[v] = (ans[u] * factor) % MOD
                queue.append(v)
                
        return ans
