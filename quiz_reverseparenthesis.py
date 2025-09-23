class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur = []
        for ch in s:
            if ch == '(':
                stack.append(cur)
                cur = []
            elif ch == ')':
                cur.reverse()
                prev = stack.pop()
                cur = prev + cur
            else:
                cur.append(ch)
        return "".join(cur)
