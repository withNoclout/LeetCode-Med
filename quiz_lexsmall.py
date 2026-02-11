class Solution(object):
    def lexSmallest(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # Initialize ans with s (equivalent to k=1 reversal, which changes nothing)
        ans = s
        
        # Try all possible lengths k from 1 to n
        for k in range(1, n + 1):
            # Option 1: Reverse the first k characters
            # s[:k] reversed + s[k:]
            cand1 = s[:k][::-1] + s[k:]
            if cand1 < ans:
                ans = cand1
            
            # Option 2: Reverse the last k characters
            # s[:-k] + s[-k:] reversed
            # Note: s[:-k] handles the prefix correctly (empty if k=n)
            cand2 = s[:-k] + s[-k:][::-1]
            if cand2 < ans:
                ans = cand2
                
        return ans
