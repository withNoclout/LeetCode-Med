from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        res = []
        
        # We only need to start from indices 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            count = 0
            
            # Slide the window across the string
            while right + word_len <= len(s):
                # Get the word from the right side of the window
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_counts:
                    current_counts[word] += 1
                    count += 1
                    
                    # If we have more of 'word' than required, slide 'left' to the right
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If the window size matches the total length of all words
                    if count == num_words:
                        res.append(left)
                else:
                    # Not a valid word, reset the window
                    current_counts.clear()
                    count = 0
                    left = right
                    
        return res
