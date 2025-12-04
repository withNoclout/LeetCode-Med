class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        res = 1
        left = 0
        cnt = 0
        for right in range(1, len(s)):
            if s[right] == s[right-1]:
                cnt += 1
            while cnt > 1:
                if s[left] == s[left+1]:
                    cnt -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
