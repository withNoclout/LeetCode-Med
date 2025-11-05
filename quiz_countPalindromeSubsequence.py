class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, last = {}, {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        ans = 0
        for c in first:
            if first[c] < last[c]:
                # Unique middle chars between first and last occurrence of c
                mid = set(s[first[c] + 1:last[c]])
                ans += len(mid)
        return ans
