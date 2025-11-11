class Solution(object):
    def getDescentPeriods(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        res = 1
        streak = 1

        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1
            res += streak

        return res
