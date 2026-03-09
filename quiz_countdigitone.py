class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        count = 0
        i = 1  # Position multiplier (1, 10, 100, ...)
        
        while i <= n:
            high = n // (i * 10)
            curr = (n // i) % 10
            low = n % i
            
            if curr == 0:
                count += high * i
            elif curr == 1:
                count += high * i + (low + 1)
            else:
                count += (high + 1) * i
            
            # Move to the next higher decimal position
            i *= 10
            
        return count
