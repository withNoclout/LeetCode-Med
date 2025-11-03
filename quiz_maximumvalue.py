class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        x = str(x)
        if n[0] == '-':
            for i in range(1, len(n)):
                if n[i] > x:
                    return n[:i] + x + n[i:]
            return n + x
        else:
            for i in range(len(n)):
                if n[i] < x:
                    return n[:i] + x + n[i:]
            return n + x
