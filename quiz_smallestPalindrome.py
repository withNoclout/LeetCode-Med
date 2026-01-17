class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # Since s is guaranteed to be a palindrome, the characters in the first half
        # (s[:n//2]) exactly represent the set of characters needed to form the pairs.
        # We simply sort them to ensure the lexicographically smallest characters come first.
        half = sorted(list(s[:n // 2]))
        
        # The middle character (if n is odd) is invariant because it's the only odd-count char.
        mid = s[n // 2] if n % 2 == 1 else ""
        
        # Construct: Smallest Half + Middle + Reversed Smallest Half
        return "".join(half) + mid + "".join(half[::-1])
