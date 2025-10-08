class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        shifts = [0] * 26
        for i in range(len(s)):
            diff = (ord(t[i]) - ord(s[i])) % 26
            if diff != 0:
                shifts[diff] += 1
                # each same shift needs +26 each repeat
                if diff + 26 * (shifts[diff] - 1) > k:
                    return False
        return True
