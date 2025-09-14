class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res=  set()
        i = 0 
        while x**i < bound : 
            j = 0 
            while x**i + y**j <= bound : 
                res.add(x**i + y**j)
                if y == 1 : break
                j += 1 
            if x == 1 : break
            i += 1  
        return list(res)
