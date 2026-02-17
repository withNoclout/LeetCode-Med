class Solution(object):
    def minAllOneMultiple(self, k):
        """
        :type k: int
        :rtype: int
        """
        # A number consisting only of the digit '1' ends in 1.
        # It cannot be divisible by 2 (even numbers) or 5 (ends in 0 or 5).
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        # Start with length 1 (value 1)
        remainder = 0
        
        # Iterate to check lengths 1, 2, 3...
        # We are guaranteed to find a solution within K iterations if K is not divisible by 2 or 5.
        for length in range(1, k + 1):
            # Update remainder for the next repunit: next_val = prev_val * 10 + 1
            remainder = (remainder * 10 + 1) % k
            
            if remainder == 0:
                return length
                
        return -1
