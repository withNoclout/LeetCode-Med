class Solution(object):
    def numOfSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Helper function to count subsequences of length 2 (e.g., "LC" or "CT")
        def calc(t):
            cnt = 0
            a = 0
            for c in s:
                if c == t[1]:
                    cnt += a
                if c == t[0]:
                    a += 1
            return cnt

        l = 0
        r = s.count('T')
        ans = 0
        mx = 0
        
        # Pass 1: Count existing "LCT" and calculate max gain for inserting 'C'
        for c in s:
            if c == 'T':
                r -= 1
            
            if c == 'C':
                ans += l * r
            
            if c == 'L':
                l += 1
            
            # Maximize gain if we insert 'C' at the current position
            mx = max(mx, l * r)
            
        # Pass 2 & 3 (via helper): Maximize gain for inserting 'L' (count "CT") or 'T' (count "LC")
        mx = max(mx, calc("LC"), calc("CT"))
        
        return ans + mx
