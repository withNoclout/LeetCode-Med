class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        inf = float('inf')
        
        # dp[i][j] stores the min cost to reach cell (i, j)
        dp = [[inf] * n for _ in range(m)]
        
        # Base Case: Start at (0, 0). Cost includes the starting cell's value.
        dp[0][0] = grid[0][0]
        
        # Helper function to propagate Right/Down moves across the grid
        def propagate_moves(current_dp):
            for i in range(m):
                for j in range(n):
                    current_val = current_dp[i][j]
                    if current_val == inf:
                        continue
                        
                    # Move Down
                    if i + 1 < m:
                        new_cost = current_val + grid[i+1][j]
                        if new_cost < current_dp[i+1][j]:
                            current_dp[i+1][j] = new_cost
                            
                    # Move Right
                    if j + 1 < n:
                        new_cost = current_val + grid[i][j+1]
                        if new_cost < current_dp[i][j+1]:
                            current_dp[i][j+1] = new_cost

        # 1. Initial pass with 0 teleports (only Right/Down moves)
        propagate_moves(dp)
        
        # 2. Iterate k times to allow up to k teleports
        for _ in range(k):
            # Step A: Find the minimum cost to reach ANY cell with value >= V.
            # This allows us to jump FROM that cell TO any cell with value <= V.
            
            # Map: value -> min_cost to reach a cell with that value
            min_cost_by_val = {}
            for r in range(m):
                for c in range(n):
                    val = grid[r][c]
                    cost = dp[r][c]
                    if val not in min_cost_by_val or cost < min_cost_by_val[val]:
                        min_cost_by_val[val] = cost
            
            # Create a "Suffix Min" map.
            # best_source_cost[v] = min(cost of any cell with value >= v)
            # If we are at a cell with value X (>= v), we can teleport to a cell with value v.
            sorted_vals = sorted(min_cost_by_val.keys(), reverse=True)
            best_source_cost = {}
            running_min = inf
            
            for v in sorted_vals:
                if min_cost_by_val[v] < running_min:
                    running_min = min_cost_by_val[v]
                best_source_cost[v] = running_min
            
            # Step B: Apply Teleports
            # Update dp[i][j] if we can teleport to it from a better source
            updated = False
            for r in range(m):
                for c in range(n):
                    val = grid[r][c]
                    # To land at 'val', we need a source with value >= val.
                    # The cost to land is exactly the cost of that source (teleport is free).
                    if val in best_source_cost:
                        teleport_cost = best_source_cost[val]
                        if teleport_cost < dp[r][c]:
                            dp[r][c] = teleport_cost
                            updated = True
            
            # Step C: Propagate moves again with the new teleported starts
            if updated:
                propagate_moves(dp)
            else:
                break
                
        return dp[m-1][n-1]
