class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        
        # Case 1: Substrings with 1 distinct character
        # We just need the longest contiguous run of identical characters.
        current_len = 0
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                current_len += 1
            else:
                current_len = 1
            ans = max(ans, current_len)
            
        # Case 2: Substrings with exactly 2 distinct characters (e.g., 'a' and 'b')
        # We treat one char as +1 and the other as -1. The third char acts as a reset delimiter.
        def solve_pair(c1, c2):
            res = 0
            # map stores { balance : first_index }
            # Initial state: balance 0 at index -1
            mp = {0: -1}
            diff = 0
            
            for i, char in enumerate(s):
                if char == c1:
                    diff += 1
                elif char == c2:
                    diff -= 1
                else:
                    # If we hit the third character (neither c1 nor c2), the chain breaks.
                    # Reset the map and balance starting from current index i.
                    mp = {0: i}
                    diff = 0
                    continue
                
                if diff in mp:
                    res = max(res, i - mp[diff])
                else:
                    mp[diff] = i
            return res

        # Check all combinations of 2 characters
        ans = max(ans, solve_pair('a', 'b'))
        ans = max(ans, solve_pair('b', 'c'))
        ans = max(ans, solve_pair('c', 'a'))
        
        # Case 3: Substrings with exactly 3 distinct characters
        # We need count(a) == count(b) == count(c).
        # We track the relative differences: (count(a) - count(b)) and (count(b) - count(c)).
        # If this tuple state repeats, the substring between occurrences is balanced for all 3.
        mp = {(0, 0): -1}
        ca = cb = cc = 0
        
        for i, char in enumerate(s):
            if char == 'a': ca += 1
            elif char == 'b': cb += 1
            elif char == 'c': cc += 1
            
            # State captures the relative balance
            state = (ca - cb, cb - cc)
            
            if state in mp:
                ans = max(ans, i - mp[state])
            else:
                mp[state] = i
                
        return ans 
