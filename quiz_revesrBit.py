class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        # We must loop exactly 32 times because the input is a 32-bit integer.
        # If we stopped when n became 0, we would miss the trailing zeros 
        # in the reversed version (which were leading zeros in the original).
        for _ in range(32):
            # 1. Shift result to the left to open up the LSB spot
            ans = ans << 1
            
            # 2. Get the last bit of n (n & 1)
            # 3. Add it to the open LSB spot in ans
            bit = n & 1
            ans = ans | bit
            
            # 4. Shift n to the right to process the next bit
            n = n >> 1
            
        return ans
