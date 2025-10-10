from collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s).values()
        used = set()
        deletions = 0
        for f in freq:
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            if f > 0:
                used.add(f)
        return deletions
