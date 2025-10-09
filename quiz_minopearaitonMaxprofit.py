class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        waiting = 0
        profit = 0
        max_profit = 0
        res = -1
        i = 0
        n = len(customers)
        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
            boarded = min(4, waiting)
            waiting -= boarded
            profit += boarded * boardingCost - runningCost
            if profit > max_profit:
                max_profit = profit
                res = i + 1
            i += 1
        return res
