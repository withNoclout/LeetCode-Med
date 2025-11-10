class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        total = 0
        for i, ch in enumerate(word):
            if ch in vowels:
                # this vowel appears in all substrings that include index i
                total += (i + 1) * (n - i)
        return total
