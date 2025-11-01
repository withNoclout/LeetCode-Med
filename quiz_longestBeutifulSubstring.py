class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = 0
        count = 1
        unique = 1
        for i in range(1, len(word)):
            if word[i] >= word[i - 1]:
                count += 1
                if word[i] != word[i - 1]:
                    unique += 1
            else:
                count = 1
                unique = 1
            if unique == 5:
                res = max(res, count)
        return res

