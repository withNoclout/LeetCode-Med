class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # dp[i] represents the minimum cost to reach step n starting from step i.
        # Initialize with infinity, base case: cost at step n is 0.
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        
        # Iterate backwards from n-1 down to 0
        for i in range(n - 1, -1, -1):
            # Try all allowed jumps: +1, +2, +3
            # Ensure j does not exceed n
            for j in range(i + 1, min(n + 1, i + 4)):
                # Calculate cost: 
                # (cost from j to n) + (cost of step j) + (penalty (j-i)^2)
                current_val = dp[j] + costs[j-1] + (j - i) * (j - i)
                
                if current_val < dp[i]:
                    dp[i] = current_val
                    
        return dp[0]
