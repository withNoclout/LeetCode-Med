class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Result is the Gray-to-binary conversion of n.
        res = 0
        while n:
            res ^= n
            n >>= 1
        return res
