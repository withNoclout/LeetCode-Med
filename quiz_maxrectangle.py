class Solution(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Convert to set for O(1) lookup
        point_set = set((x, y) for x, y in points)
        n = len(points)
        max_a = -1
        
        # Iterate through all pairs of points to define the diagonal
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]
                
                # We strictly assume (x1, y1) is bottom-left and (x2, y2) is top-right
                if x1 >= x2 or y1 >= y2:
                    continue
                
                # Check if the other two corners exist to form a rectangle
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    
                    # Validate the constraint: No other point should be inside or on the border
                    valid_rect = True
                    for k in range(n):
                        px, py = points[k]
                        
                        # Check if current point is within the rectangle boundaries (inclusive)
                        if x1 <= px <= x2 and y1 <= py <= y2:
                            # If the point is NOT one of the 4 corners, the rectangle is invalid
                            if (px, py) not in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                                valid_rect = False
                                break
                    
                    if valid_rect:
                        max_a = max(max_a, (x2 - x1) * (y2 - y1))
                        
        return max_a
