class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        cnt = {}
        ans = 0
        l = 0
        
        for r in range(n):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            
            while cnt[s[r]] >= k:
                ans += n - r
                cnt[s[l]] -= 1
                l += 1
                
        return ans
