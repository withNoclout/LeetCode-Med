class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        n=  len(arr1) 
        res = 0 
        for a , b in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            max_v = -float('inf')
            min_v = float('inf')
            for i in range(n):
                val = a*arr1[i] + b*arr2[i] + i
                max_v = max(max_v,val)
                min_v = min(min_v,val)
            res = max(res,max_v - min_v)

        return res 
