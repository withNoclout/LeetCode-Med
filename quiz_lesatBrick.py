from collections import defaultdict 
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edge = defaultdict(int)

        for row in wall : 
            pos = 0 
            for brick in row[:-1 ] : 
                pos +=  brick 
                edge[pos] += 1 

        if not edge : 
            return len(wall)
        return len(wall) - max(edge.values())
    
        max_edge = max(edge.values()) if edge else 0 

        return len(wall ) - max_edge
