class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        # Map to store the maximum y value for each unique x value
        # Key: x[i], Value: max(y[i]) for that x
        max_y_for_x = {}
        
        for val_x, val_y in zip(x, y):
            # If we haven't seen this x, or if current y is larger than stored y
            if val_x not in max_y_for_x or val_y > max_y_for_x[val_x]:
                max_y_for_x[val_x] = val_y
                
        # We need at least 3 distinct x values to form a valid triplet
        if len(max_y_for_x) < 3:
            return -1
            
        # Extract the best y values and sort them in descending order
        best_y_values = sorted(max_y_for_x.values(), reverse=True)
        
        # The answer is the sum of the top 3 largest y values
        return sum(best_y_values[:3])
