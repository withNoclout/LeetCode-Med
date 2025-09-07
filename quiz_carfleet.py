class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip( position , speed  ) , reverse=True) 
        fleets =  0 
        last_time = 0.0 

        for pos , spd in cars : 
            time = ( target - pos ) / spd 
            if time > last_time : 
                fleets  += 1 
                last_time =  t
        return fleets 
    
