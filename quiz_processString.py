def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Use a list of characters for efficient mutation
        res = []
        
        for char in s:
            if char.isalpha():
                # Append lowercase English letters
                res.append(char)
            elif char == '*':
                # Delete the last character if it exists
                if res:
                    res.pop()
            elif char == '#':
                # Duplicate the current string
                res.extend(res)
            elif char == '%':
                # Reverse the current string
                res.reverse()
                
        return "".join(res)
