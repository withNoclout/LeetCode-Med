class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num  ) ) 

        last = {int(d) : i for i  , d  in enumerate(digits ) }  

        for i , d in enumerate(digits ) : 
            for bigger in range(9 , int(d) , -1) :
                if bigger in last :
                    j = last[bigger]
                    if j > i :
                        digits[i] , digits[j] = digits[j] , digits[i]
                        return int("".join(digits))
        return num  
    
