class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        # Reverse the string
        rev_s = s[::-1]
        
        # Create a combined string with a separator to avoid overlap issues
        # The separator '#' ensures the prefix and suffix don't cross the boundary
        combined = s + "#" + rev_s
        
        # Build the KMP LPS (Longest Prefix Suffix) table
        lps = [0] * len(combined)
        for i in range(1, len(combined)):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
            
        # The last element of lps gives the length of the longest palindromic prefix
        longest_palindromic_prefix_len = lps[-1]
        
        # Take the part of rev_s that isn't part of the palindromic prefix
        # and prepend it to the original string s
        suffix_to_add = rev_s[:len(s) - longest_palindromic_prefix_len]
        
        return suffix_to_add + s
