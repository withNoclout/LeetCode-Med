class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # The minimum number of deci-binary numbers needed equals
        # the maximum digit in the string.
        return max(ord(ch) - ord('0') for ch in n)
