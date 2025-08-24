class Solution(object):
    def findLongestWord(self, s, dictionary):
        def is_subsequence(x, y):
            i = j = 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    i += 1
                j += 1
            return i == len(x)

        dictionary.sort(key=lambda w: (-len(w), w))  # longest first, then lexicographically
        for word in dictionary:
            if is_subsequence(word, s):
                return word
        return ""

