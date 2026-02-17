class Solution(object):
    def countPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        
        # Dictionary to store the frequency of each canonical form
        # Key: Tuple representing the normalized word
        # Value: Count of words seen so far with that signature
        pattern_counts = defaultdict(int)
        ans = 0
        
        for word in words:
            # Determine the shift needed to align the first character to 'a' (0)
            # We treat 'a' as 0, 'b' as 1, ..., 'z' as 25.
            first_val = ord(word[0]) - ord('a')
            
            # Build the canonical signature
            signature = []
            for char in word:
                val = ord(char) - ord('a')
                # Shift backward by 'first_val' to normalize.
                # Use modulo 26 to handle the cyclic nature (e.g., a - 1 -> z)
                normalized_val = (val - first_val) % 26
                signature.append(normalized_val)
            
            # Convert list to tuple so it can be used as a dictionary key
            signature_tuple = tuple(signature)
            
            # If this signature has appeared before, the current word forms a pair
            # with all previous instances. Add that count to the answer.
            ans += pattern_counts[signature_tuple]
            
            # Register the current word's signature for future matches
            pattern_counts[signature_tuple] += 1
            
        return ans
