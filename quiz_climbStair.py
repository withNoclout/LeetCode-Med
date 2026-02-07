class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # dp[i] stores the minimum cost to reach step i
        # Initialize with infinity, except step 0 which costs 0
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Number of possible jump types (1 step, 2 steps, ..., k steps)
        # costs[j] is the cost to jump j+1 steps
        k = len(costs)
        
        for i in range(1, n + 1):
            # Try all jump sizes j (from 1 to k)
            for j in range(1, k + 1):
                # If we can reach step i from step i-j
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i - j] + costs[j - 1])
                    
        return dp[n]
