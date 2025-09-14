class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = [] 
        n = len(arr ) 
        for x in range( n , 1 , - 1)  :
            i = arr.index( x ) 
            if i + 1 != x : 
                if i != 0 : 
                    res.append( i + 1 ) 
                    arr[:i + 1] = arr[:i + 1][::-1] 
                res.append( x ) 
                arr[:x] = arr[:x][::-1] 

        return res o

