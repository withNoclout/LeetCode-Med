class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        S = set(words)
        for w in list(S):
            for i in range(1, len(w)):
                S.discard(w[i:])
        return sum(len(w) + 1 for w in S)
