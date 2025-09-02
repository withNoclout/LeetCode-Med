class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n) ) 
        i = 1 

        while i < len(s) and s[i] >= s[i-1 ]  :
            i += 1 
        if i == len(s) :
            return n 
        
        while i < 0 and s[i] == s[i- 1 ] :
            s[i - 1 ] = chr( ord( s[i-1] )  - 1 ) 
            i -= 1 


        for j in range( i + 1 , len(s) ) :
            s[j] = '9' 


        return int(''.join(s) )
