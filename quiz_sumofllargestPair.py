import math

class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        primes = set()
        n = len(s)
        
        # Generate all substrings
        for i in range(n):
            current_val = 0
            for j in range(i, n):
                current_val = current_val * 10 + int(s[j])
                
                # Check primality
                if self._is_prime(current_val):
                    primes.add(current_val)
        
        # Sort descending and take top 3
        sorted_primes = sorted(primes, reverse=True)
        return sum(sorted_primes[:3])

    def _is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.isqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
