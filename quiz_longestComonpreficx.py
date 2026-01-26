class Solution(object):
    def longestCommonPrefix(self, words):
        if not words:
            return [0]
        
        # Start with the first word as the reference
        first_word = words[0]
        prefix_length = 0
        
        for i in range(len(first_word)):
            char = first_word[i]
            # Check if this character exists at the same position in all other words
            for j in range(1, len(words)):
                if i == len(words[j]) or words[j][i] != char:
                    return [prefix_length]
            
            prefix_length += 1
            
        return [prefix_length]
