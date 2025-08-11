class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s : 
            return 0 
        stack = []
        num = 0
        sign = '+'
        n = len(s)

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            if (not ch.isdigit() and ch != ' ') or i == n - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # truncate toward zero
                sign = ch
                num = 0

        return sum(stack)
