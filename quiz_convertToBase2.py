class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
        res = []
        while n != 0:
            n, r = divmod(n, -2)
            if r < 0:
                n += 1
                r += 2
            res.append(str(r))
        return ''.join(res[::-1])
