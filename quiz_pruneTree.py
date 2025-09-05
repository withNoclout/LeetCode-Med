class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        if num1 == 0 :
            return 0 
        
        for k in range( 1, 61 ) : 
            s = num1 - k * num2 
            if s < 0 :
                return -1

            if (bin(s).count('1') <= k and (k <= s)):
                return k
        return -1
