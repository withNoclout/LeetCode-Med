class Solution(object):
    def minEnd(self, n, x):
        n -= 1
        b = 1
        while n > 0:
            while x & b:
                b <<= 1
            if n & 1:
                x |= b
            n >>= 1
            b <<= 1
        return x
