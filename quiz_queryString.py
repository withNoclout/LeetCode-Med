class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        for k in range( n , 0 , - 1 ) :
            if bin(k)[2:] not in s:
                return False    
            
        return True 
