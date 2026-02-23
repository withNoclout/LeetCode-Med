class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur_line = []
        cur_len = 0 # Length of characters in cur_line (without spaces)
        
        for word in words:
            # Check if adding the next word exceeds the maxWidth.
            # len(cur_line) represents the minimum number of spaces required (1 between each word).
            if cur_len + len(word) + len(cur_line) > maxWidth:
                
                # We need to format the current line and add it to results.
                # Total spaces we need to distribute across the line:
                spaces_to_add = maxWidth - cur_len
                
                # Distribute spaces evenly (round-robin style)
                for i in range(spaces_to_add):
                    # gap_index determines which word gets the space appended to it.
                    # We use `len(cur_line) - 1` because we don't add spaces after the last word.
                    # The `or 1` handles the edge case where there is only 1 word on the line.
                    gap_index = i % (len(cur_line) - 1 or 1)
                    cur_line[gap_index] += " "
                    
                res.append("".join(cur_line))
                
                # Reset for the new line
                cur_line = []
                cur_len = 0
                
            cur_line.append(word)
            cur_len += len(word)
            
        # Handle the very last line (Left-justified)
        last_line = " ".join(cur_line)
        # Pad the right side with spaces until it hits maxWidth
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res
