from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        c1, c2 = Counter(word1), Counter(word2)
        if set(c1.keys()) != set(c2.keys()):
            return False
        return sorted(c1.values()) == sorted(c2.values())
