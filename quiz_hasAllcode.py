class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # The total number of required unique substrings is 2^k
        required_count = 1 << k
        
        # Optimization: If the string is too short to possibly contain 
        # all combinations, return False immediately.
        if len(s) < required_count + k - 1:
            return False
            
        seen = set()
        
        # Slide a window of size k across the string
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            
            # Early exit: If we've found all possible combinations, stop searching
            if len(seen) == required_count:
                return True
                
        # Return True only if we found exactly 2^k unique combinations
        return len(seen) == required_count
