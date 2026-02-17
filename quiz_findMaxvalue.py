class Solution(object):
    def findMaxVal(self, n, restrictions, diff):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type diff: List[int]
        :rtype: int
        """
        # Initialize the array with infinity to represent no initial upper bound
        max_vals = [float('inf')] * n
        
        # Apply the fixed anchor constraint
        max_vals[0] = 0
        
        # Apply the explicit restrictions given in the input
        for idx, val in restrictions:
            max_vals[idx] = min(max_vals[idx], val)
            
        # Forward Pass: Propagate constraints from left to right
        # Ensure a[i] <= a[i-1] + diff[i-1]
        for i in range(1, n):
            max_vals[i] = min(max_vals[i], max_vals[i-1] + diff[i-1])
            
        # Backward Pass: Propagate constraints from right to left
        # Ensure a[i] <= a[i+1] + diff[i]
        # Iterate backwards from n-2 down to 0
        for i in range(n - 2, -1, -1):
            max_vals[i] = min(max_vals[i], max_vals[i+1] + diff[i])
            
        # The result is the maximum value found in the valid sequence
        return max(max_vals)
