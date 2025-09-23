import math

class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def count(x):
            # count how many numbers <= x are divisible by a, b, or c
            ab = a * b // math.gcd(a, b)
            bc = b * c // math.gcd(b, c)
            ac = a * c // math.gcd(a, c)
            abc = ab * c // math.gcd(ab, c)
            return (x // a) + (x // b) + (x // c) - (x // ab) - (x // bc) - (x // ac) + (x // abc)

        lo, hi = 1, 2 * 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
