class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        num = 0
        sign = 1 # 1 for positive, -1 for negative
        
        for char in s:
            if char.isdigit():
                # Form the full number if it has multiple digits
                num = num * 10 + int(char)
                
            elif char in "+-":
                # Add the finished number to the result before changing sign
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1
                
            elif char == "(":
                # Push the current result and sign onto stack to solve the inner part
                stack.append(res)
                stack.append(sign)
                # Reset for the new expression inside parentheses
                res = 0
                sign = 1
                
            elif char == ")":
                # Finalize the expression inside the parentheses
                res += sign * num
                num = 0
                # res is currently the sum of everything inside the (...)
                # Multiply it by the sign before the opening '('
                res *= stack.pop()
                # Add it to the result calculated before the '('
                res += stack.pop()
                
        # Final addition for any number remaining at the end of the string
        return res + (sign * num)
