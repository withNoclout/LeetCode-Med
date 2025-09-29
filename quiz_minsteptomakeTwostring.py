class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        from collections import Counter

        cs, ct = Counter(s), Counter(t)
        steps = 0
        for ch in cs:
            if cs[ch] > ct[ch]:
                steps += cs[ch] - ct[ch]
        return steps
