class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # Helper function to check if we can form at least 3 disjoint components
        # along a specific axis.
        def has_three_components(intervals):
            # Sort intervals by their start coordinate
            intervals.sort()
            
            count = 0
            max_end = -1
            
            for start, end in intervals:
                if max_end == -1:
                    # Initialize the first component
                    count = 1
                    max_end = end
                elif start >= max_end:
                    # Found a gap (or touching boundary) between the previous block 
                    # and the current interval. This marks a valid cut position.
                    # Start a new component.
                    count += 1
                    max_end = end
                else:
                    # Overlap: extend the current component
                    max_end = max(max_end, end)
            
            # If we have 3 or more disjoint components, we can make 2 cuts 
            # (one between 1st-2nd, one between 2nd-3rd).
            return count >= 3

        # Extract intervals for X axis and Y axis
        # rect is [x1, y1, x2, y2]
        x_intervals = [(r[0], r[2]) for r in rectangles]
        y_intervals = [(r[1], r[3]) for r in rectangles]
        
        # Check if either axis allows for 3 disjoint components
        return has_three_components(x_intervals) or has_three_components(y_intervals)
