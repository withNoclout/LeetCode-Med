class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will be a dictionary mapping { current_cost : max_twos_count }
        # This handles sparse states efficiently.
        dp = [[{} for _ in range(n)] for _ in range(m)]
        
        # Initialize start cell (0, 0)
        start_val = grid[0][0]
        start_cost = 1 if start_val > 0 else 0
        start_twos = 1 if start_val == 2 else 0
        
        if start_cost <= k:
            dp[0][0][start_cost] = start_twos
        else:
            return -1 # Cannot even enter the first cell
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = grid[i][j]
                cost_inc = 1 if val > 0 else 0
                twos_inc = 1 if val == 2 else 0
                
                current_states = dp[i][j]
                
                # Function to transition from a previous cell (prev_i, prev_j)
                def merge(prev_i, prev_j):
                    if 0 <= prev_i < m and 0 <= prev_j < n:
                        prev_states = dp[prev_i][prev_j]
                        for c, t in prev_states.items():
                            new_c = c + cost_inc
                            if new_c <= k:
                                new_t = t + twos_inc
                                # Keep the max 'twos' for this specific cost
                                if new_c not in current_states or new_t > current_states[new_c]:
                                    current_states[new_c] = new_t

                # Try coming from Top
                merge(i - 1, j)
                # Try coming from Left
                merge(i, j - 1)
                
        # Check the destination cell
        final_states = dp[m-1][n-1]
        
        if not final_states:
            return -1
            
        ans = -1
        # Score = Cost + Count of 2s
        for c, t in final_states.items():
            ans = max(ans, c + t)
            
        return ans
