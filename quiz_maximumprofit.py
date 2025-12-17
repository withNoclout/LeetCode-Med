class Solution(object):
    def maximumProfit(self, prices, k):
        n = len(prices)
        if n <= 1:
            return 0
        
        # If k is large enough to cover all profitable transactions
        if 2 * k >= n:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
            
        # dp[i][0]: Max profit with i transactions, currently holding stock
        # dp[i][1]: Max profit with i transactions, currently not holding stock
        dp = [[-float('inf'), 0] for _ in range(k + 1)]
        
        for price in prices:
            for i in range(1, k + 1):
                # Buy: Max of (keep holding, buy new using profit from previous transaction)
                dp[i][0] = max(dp[i][0], dp[i-1][1] - price)
                # Sell: Max of (keep not holding, sell current holding)
                dp[i][1] = max(dp[i][1], dp[i][0] + price)
                
        return dp[k][1]
