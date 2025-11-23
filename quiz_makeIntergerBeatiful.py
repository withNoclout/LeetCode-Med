class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        n0 = n
        base = 1
        while sum(int(c) for c in str(n)) > target:
            n = n // 10 + 1
            base *= 10
        return n * base - n0
