class Solution(object):
    def __init__(self):
        # Dictionary to cache results of previously seen (s1, s2) pairs
        self.memo = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Check cache first
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
            
        # Base case: perfect match
        if s1 == s2:
            self.memo[(s1, s2)] = True
            return True
            
        # Pruning step: if the characters don't match perfectly, it's impossible
        # Sorting is fast enough for small lengths (<= 30), or use collections.Counter
        if sorted(s1) != sorted(s2):
            self.memo[(s1, s2)] = False
            return False
            
        n = len(s1)
        
        # Try splitting the string at every possible index from 1 to n-1
        for i in range(1, n):
            
            # Condition 1: Substrings are NOT swapped
            # Check s1[0:i] with s2[0:i] AND s1[i:n] with s2[i:n]
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[(s1, s2)] = True
                return True
                
            # Condition 2: Substrings ARE swapped
            # Check s1[0:i] with s2[n-i:n] AND s1[i:n] with s2[0:n-i]
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.memo[(s1, s2)] = True
                return True
                
        # If no split works, it's not a scramble
        self.memo[(s1, s2)] = False
        return False
