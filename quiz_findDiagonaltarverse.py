class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0] : 
            return [] 
        
        m  , n = len(mat ) , len(mat[0])
        res = [] 
        for d in range( m+ n - 1 ) : 
            intermidate = []
            r =  0 if d < n else d - n + 1 
            c = d if d < n else n - 1

            while r < n and c >= 0:
                intermidate.append(mat[r][c])
                r+= 1 
                c -= 1 

            if d % 2 == 0:
                res.extend(intermidate[::-1])
            else : 
                res.extend(intermidate)

        return res 
