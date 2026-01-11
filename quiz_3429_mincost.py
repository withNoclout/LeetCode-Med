class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minCost(self, n, cost):
        # dp[i][color1][color2] represents the minimum cost for the first i pairs
        # where the i-th element from the start has color1 
        # and the i-th element from the end has color2.
        
        # Initialize DP table with infinity
        # Since n is even, we only need to iterate up to n // 2
        m = n // 2
        dp = [[float('inf')] * 3 for _ in range(3)]
        
        # Base case: first pair (0 and n-1)
        for c1 in range(3):
            for c2 in range(3):
                if c1 != c2:
                    dp[c1][c2] = cost[0][c1] + cost[n - 1][c2]
        
        for i in range(1, m):
            new_dp = [[float('inf')] * 3 for _ in range(3)]
            for pc1 in range(3): # previous color 1
                for pc2 in range(3): # previous color 2
                    if dp[pc1][pc2] == float('inf'):
                        continue
                    
                    for c1 in range(3): # current color 1
                        for c2 in range(3): # current color 2
                            # Conditions: 
                            # 1. current pair colors are different (c1 != c2)
                            # 2. current c1 != previous c1 (c1 != pc1)
                            # 3. current c2 != previous c2 (c2 != pc2)
                            if c1 != c2 and c1 != pc1 and c2 != pc2:
                                current_cost = cost[i][c1] + cost[n - 1 - i][c2]
                                new_dp[c1][c2] = min(new_dp[c1][c2], dp[pc1][pc2] + current_cost)
            dp = new_dp
            
        ans = float('inf')
        for r in dp:
            ans = min(ans, min(r))
        return ans
