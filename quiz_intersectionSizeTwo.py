class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # 1. Sort the intervals:
        # Primary key: end point (ascending)
        # Secondary key: start point (descending) - This is crucial for the greedy choice
        # Sorting ensures we satisfy the most restrictive intervals first.
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # p1 and p2 store the two largest points currently in the intersection set S, with p1 < p2.
        # Initialize them to values guaranteed to be outside the first interval.
        p1 = -1
        p2 = -1
        size = 0
        
        for start, end in intervals:
            
            # Check the current interval [start, end] against the two current largest points (p1, p2)
            
            # Case 1: [start, end] is NOT satisfied at all (0 intersection points)
            # This occurs if the start is greater than the largest point p2.
            if start > p2:
                # We need to add two points: b-1 and b.
                p1 = end - 1
                p2 = end
                size += 2
                
            # Case 2: [start, end] is partially satisfied (1 intersection point)
            # This occurs if start <= p2, but start > p1.
            # The one point is p2.
            elif start > p1:
                # We need to add one more point. The best choice is the largest possible: b.
                # Since p1 must be < p2, the new pair must be the smaller of the old pair (p2)
                # and the new point (b). We know start <= p2 and start <= b, 
                # and we need to keep the two largest.
                
                # The existing largest point is p2. The new point is 'end'. 
                # The new pair of largest points will be (p2, end).
                p1 = p2 # The old largest point becomes the new smaller point
                p2 = end # The new point is the largest
                size += 1
                
            # Case 3: [start, end] is fully satisfied (2 intersection points or more)
            # This occurs if start <= p1 (since p1 < p2, start <= p2 is also true).
            # Do nothing and move to the next interval.
            
        return size
