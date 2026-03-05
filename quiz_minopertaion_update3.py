class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        # We compare the input string against the pattern starting with '0' (0101...)
        # At even indices (0, 2, 4...), we expect '0'.
        # At odd indices (1, 3, 5...), we expect '1'.
        
        count_start_zero = 0
        n = len(s)
        
        for i in range(n):
            # Check if the character matches the pattern starting with '0'
            # i % 2 gives 0 for even indices and 1 for odd indices.
            # We convert it to a string to compare with s[i].
            if s[i] != str(i % 2):
                count_start_zero += 1
        
        # The number of operations to reach the pattern starting with '1' 
        # is simply (total length - operations for pattern starting with '0').
        return min(count_start_zero, n - count_start_zero)
