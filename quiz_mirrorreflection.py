import math

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        g = math.gcd(p, q)
        p //= g
        q //= g
        if p % 2 == 0 and q % 2 == 1:
            return 2
        if p % 2 == 1 and q % 2 == 1:
            return 1
        return 0
