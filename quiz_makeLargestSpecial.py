class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        i = 0
        components = []
        
        # Iterate through the string to find valid top-level special substrings
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            
            # When count is 0, we found a complete valid special string s[i:j+1]
            if count == 0:
                # The substring is '1' + inner + '0'. 
                # We recursively find the largest special string for the inner part.
                inner = self.makeLargestSpecial(s[i+1:j])
                components.append('1' + inner + '0')
                
                # Move the start pointer for the next component
                i = j + 1
                
        # Sort the components in descending order to make it lexicographically largest
        components.sort(reverse=True)
        
        # Join the sorted components back into a single string
        return "".join(components)
