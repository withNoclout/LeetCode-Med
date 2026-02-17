class Solution(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        # Initialize with default "not found" values
        best_coord = [-1, -1]
        max_quality = -1
        
        cx, cy = center
        
        for x, y, q in towers:
            # Calculate Manhattan Distance
            dist = abs(x - cx) + abs(y - cy)
            
            # Check reachability
            if dist <= radius:
                # Check if this tower is better than the current best
                # Condition 1: Higher quality
                if q > max_quality:
                    max_quality = q
                    best_coord = [x, y]
                # Condition 2: Same quality, but lexicographically smaller coordinate
                elif q == max_quality:
                    # If best_coord is [-1, -1], any valid tower is better.
                    # Otherwise, compare coordinates.
                    if best_coord == [-1, -1] or (x < best_coord[0]) or (x == best_coord[0] and y < best_coord[1]):
                        best_coord = [x, y]
                        
        return best_coord
