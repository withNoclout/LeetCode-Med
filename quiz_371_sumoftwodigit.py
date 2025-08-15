class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        
        # if a is negative
        return a if a <= INT_MAX else ~(a ^ MASK)
