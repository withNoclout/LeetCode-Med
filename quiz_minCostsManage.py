class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        from collections import Counter 
        from heapq import nsmallest 

        freq = Counter() 
        for b in basket1 : 
            freq[b] +=1 
        for b in basket2 : 
            freq[b] -= 1 


        if any(v % 2 != 0 for v in freq.values()) :
            return -1

        excess = []

        for k in freq : 
            count = abs(freq[k]) // 2 
            excess.extend([k] * count ) 

        excess.sort()

        min_val = min( basket1 + basket2 ) 
        cost = 0 

        for i in range(len(excess) // 2 ) :
            cost += min( excess[i], min_val * 2 )

        return cost 
