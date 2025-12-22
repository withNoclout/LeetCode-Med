class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        res = 0
        i = 1
        n = len(word)
        while i < n:
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                res += 1
                i += 2
            else:
                i += 1
        return res
