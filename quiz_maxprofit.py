class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        buy1 = float('inf')
        sell1 = 0
        buy2 = float('inf')
        sell2 = 0
        
        for price in prices:
            # 1. Minimize the cost of our first purchase
            buy1 = min(buy1, price)
            
            # 2. Maximize the profit of our first sale
            sell1 = max(sell1, price - buy1)
            
            # 3. Minimize the effective cost of our second purchase 
            # (current price MINUS the profit we already made)
            buy2 = min(buy2, price - sell1)
            
            # 4. Maximize the final profit from our second sale
            sell2 = max(sell2, price - buy2)
            
        return sell2
