from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        cnt = Counter(words)
        ans = 0
        center = False

        # pairs of identical letters like "aa"
        for w, c in cnt.items():
            if w[0] == w[1]:
                ans += (c // 2) * 4
                if c % 2 == 1:
                    center = True

        # pairs of different letters like "ab" & "ba"
        for w, c in cnt.items():
            if w[0] != w[1]:
                rev = w[::-1]
                if w < rev:  # count each pair once
                    ans += min(c, cnt.get(rev, 0)) * 4

        return ans + (2 if center else 0)
