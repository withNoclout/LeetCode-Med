class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        total = 0
        while total < n:
            k += 1
            total += k
        return k
