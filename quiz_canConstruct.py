class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # If k is greater than length of string, impossible
        if k > len(s):
            return False

        # Count frequency of each character
        from collections import Counter
        freq = Counter(s)

        # Count how many characters appear odd number of times
        odd_count = sum(v % 2 for v in freq.values())

        # To form k palindromes:
        # - We need at least odd_count palindromes
        # - But cannot exceed k
        return odd_count <= k
