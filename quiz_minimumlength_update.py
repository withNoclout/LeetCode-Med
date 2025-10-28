class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            ch = s[i]
            while i <= j and s[i] == ch:
                i += 1
            while j >= i and s[j] == ch:
                j -= 1
        return j - i + 1
