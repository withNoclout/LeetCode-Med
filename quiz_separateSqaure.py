class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0
        
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)
        
        # Binary search for the split line
        for _ in range(70):  # Sufficient iterations for precision
            mid = (low + high) / 2.0
            area_below = 0
            for _, y, l in squares:
                # Calculate height of square below the line 'mid'
                h = max(0.0, min(float(l), mid - y))
                area_below += h * l
            
            if area_below < target:
                low = mid
            else:
                high = mid
                
        return high
