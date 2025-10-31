class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        w1 = sentence1.split()
        w2 = sentence2.split()

        # Ensure w1 is the longer sentence
        if len(w1) < len(w2):
            w1, w2 = w2, w1

        i = 0
        while i < len(w2) and w1[i] == w2[i]:
            i += 1

        j = 0
        while j < len(w2) - i and w1[-1 - j] == w2[-1 - j]:
            j += 1

        return i + j == len(w2)
