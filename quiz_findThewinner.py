class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1
