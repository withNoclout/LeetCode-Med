
class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        tr = t[::-1]  # Reverse t to treat the problem as Longest Common Substring variations
        
        # Helper to find longest palindrome starting at each index
        def get_max_pal_starts(text):
            ln = len(text)
            starts = [0] * (ln + 1) # starts[i] = max len of palindrome starting at i
            # Standard center expansion
            for center in range(2 * ln - 1):
                left = center // 2
                right = left + center % 2
                while left >= 0 and right < ln and text[left] == text[right]:
                    starts[left] = max(starts[left], right - left + 1)
                    left -= 1
                    right += 1
            return starts

        # Helper to find longest palindrome ending at each index
        def get_max_pal_ends(text):
            ln = len(text)
            ends = [0] * (ln + 1) # ends[i] = max len of palindrome ending at i (exclusive)
            for center in range(2 * ln - 1):
                left = center // 2
                right = left + center % 2
                while left >= 0 and right < ln and text[left] == text[right]:
                    ends[right + 1] = max(ends[right + 1], right - left + 1)
                    left -= 1
                    right += 1
            return ends

        # 1. Precompute palindromes
        # For S, we need palindromes that can be appended AFTER a match (starting at i)
        pal_s_starts = get_max_pal_starts(s)
        
        # For T (reversed), we need palindromes that can be prepended BEFORE a match (ending at j)
        pal_tr_ends = get_max_pal_ends(tr)
        
        # 2. DP for Longest Common Substring between S and T_reversed
        # dp[i][j] stores the length of the matching suffix between s[:i] and tr[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        max_len = 0
        
        # Check pure palindromes in S and T first (effectively match len = 0)
        max_len = max(max_len, max(pal_s_starts) if s else 0, max(pal_tr_ends) if t else 0)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == tr[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    match_len = dp[i][j]
                    
                    # Current combined string: (Match in S) + (Match in T_rev)
                    # The parts are s[i-match_len : i] and tr[j-match_len : j]
                    # Structure: (Part from S) + (Middle Palindrome) + (Part from T)
                    
                    # Case 1: Palindrome exists in S immediately after the match
                    # s_sub = match + pal_s, t_sub = match_reversed
                    # Combined length: match_len * 2 + palindrome in S starting at i
                    len1 = match_len * 2 + (pal_s_starts[i] if i < n else 0)
                    
                    # Case 2: Palindrome exists in T_rev immediately before the match
                    # s_sub = match, t_sub = pal_t + match_reversed
                    # Combined length: match_len * 2 + palindrome in T_rev ending at j - match_len
                    remaining_tr_idx = j - match_len
                    len2 = match_len * 2 + (pal_tr_ends[remaining_tr_idx] if remaining_tr_idx > 0 else 0)
                    
                    max_len = max(max_len, len1, len2)
                else:
                    dp[i][j] = 0
                    
        return max_len
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) 
        dp= [ [0] * n for _ in range(n) ]  

        for i in range( n- 1 , - 1, -1 ):
            dp[i][i] = 1 
            for j in range( i + 1 , n  ) : 
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 
                else: 
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
