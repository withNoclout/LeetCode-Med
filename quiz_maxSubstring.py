class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        first = {}
        ans = 0
        
        for i, c in enumerate(word):
            if c in first:
                # Check if the substring from the first occurrence to current 'i' 
                # meets the length requirement (>= 4).
                if i - first[c] + 1 >= 4:
                    ans += 1
                    # Greedy Step: Once we pick a substring, we must ensure subsequent 
                    # substrings do not overlap. Clearing the map resets the search 
                    # window starting from the next character.
                    first.clear()
            else:
                # Record the first occurrence of the character in the current window
                first[c] = i
                
        return ans
