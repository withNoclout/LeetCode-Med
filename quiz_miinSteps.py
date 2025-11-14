from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        cs, ct = Counter(s), Counter(t)
        letters = set(cs) | set(ct)
        return sum(abs(cs.get(ch, 0) - ct.get(ch, 0)) for ch in letters)
