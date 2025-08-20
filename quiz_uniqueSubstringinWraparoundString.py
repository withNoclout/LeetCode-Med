class Solution(object):
    def findSubstringInWraproundString(self, s):
        if not s:
            return 0

        dp = [0] * 26  # dp[c] = max length of substring ending with char c
        k = 0          # current length of valid substring

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[ord(ch) - ord('a')] = max(dp[ord(ch) - ord('a')], k)

        return sum(dp)
