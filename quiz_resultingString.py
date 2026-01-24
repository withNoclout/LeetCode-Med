class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if stack:
                # Check if current char and top of stack are "consecutive"
                # Conditions:
                # 1. Absolute difference is 1 (e.g., 'a' and 'b')
                # 2. 'a' and 'z' pair (circular property)
                prev = stack[-1]
                diff = abs(ord(char) - ord(prev))
                
                if diff == 1 or diff == 25:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
                
        return "".join(stack)
