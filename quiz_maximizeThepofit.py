class Solution(object):
    def maximizeTheProfit(self, n, offers):
        dp = [0] * (n + 1)
        import collections
        groups = collections.defaultdict(list)
        
        for s, e, g in offers:
            groups[e].append((s, g))
            
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            for s, g in groups[i-1]:
                dp[i] = max(dp[i], dp[s] + g)
                
        return dp[n]
