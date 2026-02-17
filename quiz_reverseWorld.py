class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiou")
        
        def count_vowels(word):
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            return count
            
        words = s.split()
        
        if not words:
            return ""
            
        # Determine the vowel count of the first word
        target_count = count_vowels(words[0])
        
        # Iterate through the rest of the words starting from index 1
        for i in range(1, len(words)):
            # If the current word has the same number of vowels as the first word
            if count_vowels(words[i]) == target_count:
                # Reverse the word
                words[i] = words[i][::-1]
                
        # Reconstruct the sentence with single spaces
        return " ".join(words)
