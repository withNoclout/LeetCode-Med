class Solution(object):
    def smallestValue(self, n):
        while True:
            s = 0
            temp = n
            i = 2
            while i * i <= temp:
                while temp % i == 0:
                    s += i
                    temp //= i
                i += 1
            if temp > 1:
                s += temp
            if s == n:
                return n
            n = s
