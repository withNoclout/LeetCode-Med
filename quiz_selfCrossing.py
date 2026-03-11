class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        d = distance
        n = len(d)
        if n < 4: return False

        for i in range(3, n):
            # Case 1: Fourth segment crosses first
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
            
            # Case 2: Fifth segment meets first
            if i >= 4:
                if d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                    return True
            
            # Case 3: Sixth segment crosses first
            if i >= 5:
                if d[i-1] <= d[i-3] and d[i-1] + d[i-5] >= d[i-3] and \
                   d[i-2] > d[i-4] and d[i] + d[i-4] >= d[i-2]:
                    return True
        
        return False
