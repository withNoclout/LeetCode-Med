class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s= sorted( str(n) )
        for k in range(31) : 
            if s == sorted( str(1 << k) ) : return True
        return False

        
