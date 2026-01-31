# Precompute primes globally to avoid re-calculation for every test case.
MAX_N = 100005
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate diff: sum(Prime Indices) - sum(Non-Prime Indices)
        # Or simply sum all and subtract 2*non_primes, but tracking diff is cleaner.
        diff = 0
        
        # We only need to iterate up to the length of the input array
        for i, x in enumerate(nums):
            if is_prime[i]:
                diff += x
            else:
                diff -= x
                
        return abs(diff)
