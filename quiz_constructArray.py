class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [] 
        left  , right = 1 , k + 1 

        while left <= right : 
            res.append(left)  
            left += 1 

            if left <= right : 
                res.append(right ) 
                right -= 1 


        for x in range( k + 2 , n+ 1 ) :
            res.append(x) 


        return res 
