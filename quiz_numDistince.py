class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp array to store the number of ways to form prefixes of t
        dp = [0] * (len(t) + 1)
        
        # Base case: an empty target string can always be formed exactly 1 way
        dp[0] = 1
        
        # Iterate through every character in the source string s
        for i in range(len(s)):
            # Iterate backwards through the target string t
            for j in range(len(t) - 1, -1, -1):
                
                # If the characters match, we add the number of ways 
                # we could form the prefix up to the previous character
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
                    
        # The last element contains the number of ways to form the full string t
        return dp[-1]
