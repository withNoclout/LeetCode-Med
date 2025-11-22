class Solution(object):
    def longestContinuousSubstring(self, s):
        res = curr = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1
        return res
