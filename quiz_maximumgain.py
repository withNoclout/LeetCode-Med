class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_pair(s, a, b, score):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return "".join(stack), total

        res = 0
        if x >= y:
            s, t1 = remove_pair(s, 'a', 'b', x)
            _, t2 = remove_pair(s, 'b', 'a', y)
        else:
            s, t1 = remove_pair(s, 'b', 'a', y)
            _, t2 = remove_pair(s, 'a', 'b', x)
        return t1 + t2
