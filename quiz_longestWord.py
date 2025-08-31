class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()  # ensures lexicographically smallest chosen among same length
        buildable = set([""])
        best = ""
        for w in words:
            if w[:-1] in buildable:
                buildable.add(w)
                if len(w) > len(best):
                    best = w
        return best
