class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        res = 0 
        while target > startValue : 
            if target % 2 == 0 :
                target //= 2 
            else : 
                target += 1 
            res += 1
        return res + startValue - target
