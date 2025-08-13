class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold = -10** 9
        sold= 0 
        rest = 0 
        for p in prices : 
            prev_hold = hold 
            hold = max( hold, rest- p )
            rest = max(rest, sold ) 
            sold = prev_hold + p 
        return max(sold, rest )
