class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack[-3:] = []
        return not stack
