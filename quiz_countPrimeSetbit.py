class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # All possible prime numbers of set bits for 32-bit integers
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        prime_count = 0
        
        for num in range(left, right + 1):
            # bin(num) converts integer to binary string (e.g., '0b1010')
            # .count('1') counts the occurrences of '1'
            if bin(num).count('1') in primes:
                prime_count += 1
                
        return prime_count
