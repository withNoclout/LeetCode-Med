class Solution(object):
    def getDescentPeriods(self, prices):
        res = 1
        current_len = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                current_len += 1
            else:
                current_len = 1
            res += current_len
            
        return res
