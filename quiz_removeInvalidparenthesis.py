class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # BFS initialization
        queue = {s}
        while queue:
            # Check for valid strings at the current level
            valid_strings = filter(is_valid, queue)
            if valid_strings:
                return list(valid_strings)
            
            # If no valid strings, generate the next level by removing one bracket
            next_level = set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            queue = next_level
            
        return [""]
