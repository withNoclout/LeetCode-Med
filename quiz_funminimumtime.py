class Solution(object):
    def findMinimumTime(self, strength, k):
        """
        :type strength: List[int]
        :type k: int
        :rtype: int
        """
        n = len(strength)
        memo = {}
        
        def solve(mask):
            # Base case: All locks are broken
            if mask == (1 << n) - 1:
                return 0
            
            if mask in memo:
                return memo[mask]
            
            # Calculate current X factor:
            # X = 1 + (number of locks already broken * k)
            current_x = 1 + (bin(mask).count('1') * k)
            
            min_t = float('inf')
            
            for i in range(n):
                # If the i-th lock is not broken yet
                if not (mask & (1 << i)):
                    # Calculate time to break this lock: ceil(strength[i] / current_x)
                    # Using integer math: (numerator + denominator - 1) // denominator
                    time_needed = (strength[i] + current_x - 1) // current_x
                    
                    # Recurse for the next state
                    min_t = min(min_t, time_needed + solve(mask | (1 << i)))
            
            memo[mask] = min_t
            return min_t
            
        return solve(0)
