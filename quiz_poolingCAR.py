class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stops = [0] * 1001 
        for num , start , end in trips :
            stops[start ]  += num 
            stops[end ] -= num 

        curr = 0 
        for s in stops : 
            curr += s 
            if curr > capacity  :
                return False 
            
        return True 
