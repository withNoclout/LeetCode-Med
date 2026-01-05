class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        frequencies = [0] * 128
        is_vowel = [False] * 128
        for v in 'aeiou':
            is_vowel[ord(v)] = True
            
        response = 0
        current_k = 0
        vowels = 0
        extra_left = 0
        left = 0
        
        for right, char in enumerate(word):
            if is_vowel[ord(char)]:
                frequencies[ord(char)] += 1
                if frequencies[ord(char)] == 1:
                    vowels += 1
            else:
                current_k += 1
                
            while current_k > k:
                left_char = word[left]
                if is_vowel[ord(left_char)]:
                    frequencies[ord(left_char)] -= 1
                    if frequencies[ord(left_char)] == 0:
                        vowels -= 1
                else:
                    current_k -= 1
                left += 1
                extra_left = 0
                
            while vowels == 5 and current_k == k and left < right and \
                  is_vowel[ord(word[left])] and frequencies[ord(word[left])] > 1:
                extra_left += 1
                frequencies[ord(word[left])] -= 1
                left += 1
                
            if current_k == k and vowels == 5:
                response += (1 + extra_left)
                
        return response
