class Solution(object):
    def distinctPrimeFactors(self, nums):
        primes = set()
        for n in nums:
            d = 2
            while d * d <= n:
                if n % d == 0:
                    primes.add(d)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1:
                primes.add(n)
        return len(primes)
