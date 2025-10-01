class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        res , max_seen = 0 , 0 
        for i , f in enumerate( flips , 1  ) :
            max_seen = max( max_seen , f )
            if max_seen ==  i : 
                res += 1 
        return res 
