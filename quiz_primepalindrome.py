class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        if n <= 2:
            return 2
        if 3 <= n <= 3:
            return 3
        if 4 <= n <= 5:
            return 5
        if 6 <= n <= 7:
            return 7
        # No even-length palindrome > 11 is prime (divisible by 11), so jump to 11 if in range
        if 8 <= n <= 11:
            return 11

        # Generate odd-length palindromes only
        # For length L = 2*m-1, build from left half 'x' of length m: pal = x + reverse(x[:-1])
        import math
        len_n = len(str(n))
        # Start with the smallest odd length >= len_n
        m = (len_n + 1) // 2
        if len_n % 2 == 0:
            m += 1  # next odd total length

        while True:
            start = 10 ** (m - 1)
            end = 10 ** m
            for x in range(start, end):
                s = str(x)
                pal = int(s + s[-2::-1])  # mirror without the last char to make odd length
                if pal < n:
                    continue
                if is_prime(pal):
                    return pal
            m += 1  # move to next odd length
