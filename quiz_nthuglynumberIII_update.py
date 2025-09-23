class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x // gcd(x, y) * y

        def count(x):
            ab = lcm(a, b)
            bc = lcm(b, c)
            ac = lcm(a, c)
            abc = lcm(ab, c)
            return (x // a) + (x // b) + (x // c) - (x // ab) - (x // bc) - (x // ac) + (x // abc)

        lo, hi = 1, 2 * 10**18  # big enough upper bound
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo

