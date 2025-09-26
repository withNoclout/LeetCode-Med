class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = list(s)

        # First pass: mark invalid ')'
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''  # remove invalid ')'

        # Second pass: remove unmatched '('
        while stack:
            idx = stack.pop()
            s[idx] = ''

        return "".join(s)
