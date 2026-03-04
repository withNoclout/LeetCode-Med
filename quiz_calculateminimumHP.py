class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        
        # Initialize DP table with infinity
        # We use (m+1) x (n+1) to handle boundary conditions easily
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: health needed after reaching the princess is 1
        dp[m][n-1] = dp[m-1][n] = 1
        
        # Fill the DP table backwards
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Health needed to survive the next step
                min_health_needed = min(dp[i+1][j], dp[i][j+1])
                
                # Calculate required health before entering this room
                res = min_health_needed - dungeon[i][j]
                
                # Health can never drop to 0 or below; must be at least 1
                dp[i][j] = max(1, res)
        
        return dp[0][0]
