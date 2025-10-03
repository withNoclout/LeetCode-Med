class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        from math import gcd
        res = []
        for denom in range(2, n + 1):
            for num in range(1, denom):
                if gcd(num, denom) == 1:
                    res.append(str(num) + "/" + str(denom))
        return res
