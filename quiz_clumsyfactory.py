class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [n]
        n -= 1
        i = 0
        while n > 0:
            if i % 4 == 0:
                stack[-1] *= n
            elif i % 4 == 1:
                stack[-1] //= n
            elif i % 4 == 2:
                stack.append(n)
            else:
                stack.append(-n)
            n -= 1
            i += 1
        return sum(stack)
