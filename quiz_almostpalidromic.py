class Solution(object):
    def almostPalindromic(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
            
        max_len = 0
        
        # Helper to continue expanding assuming NO more skips are allowed.
        # It returns the final boundary indices (l, r) after expansion stops.
        def get_strict_palindrome_bounds(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l, r
            
        # Iterate over all possible centers
        # i is the index of the character (for odd length centers)
        # or the left side of the gap (for even length centers)
        for i in range(n):
            
            # Case 1: Odd length centers (centered at s[i])
            l, r = i, i
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    # Mismatch found. We MUST remove one character now.
                    
                    # Option A: Remove s[l]. Continue checking (l-1) vs r
                    l1, r1 = get_strict_palindrome_bounds(l - 1, r)
                    # The length is derived from the strict bounds. 
                    # The substring spans indices l1+1 to r1-1.
                    # Formula: (r1 - 1) - (l1 + 1) + 1 = r1 - l1 - 1
                    len_a = r1 - l1 - 1
                    
                    # Option B: Remove s[r]. Continue checking l vs (r+1)
                    l2, r2 = get_strict_palindrome_bounds(l, r + 1)
                    len_b = r2 - l2 - 1
                    
                    max_len = max(max_len, len_a, len_b)
                    
                    # We consumed our only allowed skip, so we must stop this center.
                    break
            else:
                # If the loop finished without hitting a mismatch, we found a perfect palindrome.
                # Perfect palindromes (e.g., "aba") are also almost-palindromic.
                max_len = max(max_len, r - l - 1)
                
            # Case 2: Even length centers (centered between s[i] and s[i+1])
            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    # Mismatch found. Same logic as above.
                    
                    # Option A: Remove s[l]
                    l1, r1 = get_strict_palindrome_bounds(l - 1, r)
                    len_a = r1 - l1 - 1
                    
                    # Option B: Remove s[r]
                    l2, r2 = get_strict_palindrome_bounds(l, r + 1)
                    len_b = r2 - l2 - 1
                    
                    max_len = max(max_len, len_a, len_b)
                    break
            else:
                max_len = max(max_len, r - l - 1)
                
        return max_len
