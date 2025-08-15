class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        if target > x + y  :
            return False 
        if target == 0 :
            return True 
        
        return target % self.gcd(x, y) == 0
