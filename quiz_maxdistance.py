class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize with the first array's min and max
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        # Iterate from the second array onward
        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]
            
            # Compare distances with previous global min and max
            max_distance = max(
                max_distance,
                abs(curr_max - min_val),
                abs(max_val - curr_min)
            )
            
            # Update global min and max
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)
        
        return max_distance
