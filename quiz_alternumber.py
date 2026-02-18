class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1. XOR n with itself shifted right by 1.
        # If n has alternating bits (e.g., 101), n >> 1 is (010).
        # 101 ^ 010 = 111. The result should be a sequence of all 1s.
        temp = n ^ (n >> 1)
        
        # 2. Check if 'temp' consists entirely of 1s.
        # If temp is all 1s (e.g., 111), adding 1 makes it a power of 2 (1000).
        # The bitwise AND of these two numbers should be 0.
        return (temp & (temp + 1)) == 0
