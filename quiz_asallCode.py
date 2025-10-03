class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        need = 1 << k   # total number of distinct binary codes of length k
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            if len(seen) == need:
                return True
        return len(seen) == need
