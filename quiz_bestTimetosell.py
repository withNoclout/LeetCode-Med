class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        hold = -prices[0]  # max profit holding a stock
        cash = 0           # max profit not holding a stock
        for p in prices[1:]:
            hold = max(hold, cash - p)
            cash = max(cash, hold + p - fee)
        return cash
