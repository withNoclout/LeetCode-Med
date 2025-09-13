class Solution(object):
    def maxFreqSum(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = {}
        consonant_count = {}
        
        # Count frequencies
        for char in s:
            if char in vowels:
                vowel_count[char] = vowel_count.get(char, 0) + 1
            else:
                consonant_count[char] = consonant_count.get(char, 0) + 1
        
        # Find maximum frequencies
        max_vowel_freq = max(vowel_count.values()) if vowel_count else 0
        max_consonant_freq = max(consonant_count.values()) if consonant_count else 0
        
        return max_vowel_freq + max_consonant_freq
