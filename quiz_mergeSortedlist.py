class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif token == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))  # Truncate toward zero
            else:
                stack.append(int(token))

        return stack[-1]
