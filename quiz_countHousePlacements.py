class Solution(object):
    def countHousePlacements(self, n):
        mod = 10**9 + 7
        
        # Fibonacci-like DP for one side
        a, b = 1, 2   # a=f(1)=1, b=f(2)=2
        if n == 1:
            return (a * a) % mod
        if n == 2:
            return (b * b) % mod

        for _ in range(3, n + 1):
            a, b = b, (a + b) % mod

        return (b * b) % mod
