class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxWeight(self, n, edges, k, t):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :type t: int
        :rtype: int
        """
        # Adjacency list for the directed graph
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dp[u] stores the set of valid path weights ending at node u
        # for the current path length (number of edges processed so far).
        # Base case: Path of length 0 at any node has weight 0.
        dp = [{0} for _ in range(n)]
        
        # Iterate exactly k times to extend paths by one edge each step
        for _ in range(k):
            new_dp = [set() for _ in range(n)]
            has_path = False
            
            # Try to extend paths from every node u
            for u in range(n):
                if not dp[u]:
                    continue
                
                # For each neighbor v, try adding the edge weight
                for v, w in adj[u]:
                    for val in dp[u]:
                        new_val = val + w
                        # Only keep paths strictly less than t
                        if new_val < t:
                            new_dp[v].add(new_val)
                            has_path = True
            
            dp = new_dp
            # Optimization: If no valid paths of this length exist, we can stop early
            if not has_path:
                return -1
                
        # Find the maximum weight among all valid paths of length k ending at any node
        ans = -1
        for s in dp:
            if s:
                ans = max(ans, max(s))
                
        return ans
