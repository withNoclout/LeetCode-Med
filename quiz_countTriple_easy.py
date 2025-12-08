class Solution(object):
    def countTriples(self, n):
        res = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                t = a * a + b * b
                c = int(t ** 0.5)
                if c * c == t and c <= n:
                    res += 1
        return res
