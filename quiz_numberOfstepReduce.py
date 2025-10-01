class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0
        n = len(s)

        # Traverse from least significant bit to most (right → left)
        for i in range(n - 1, 0, -1):
            bit = int(s[i]) + carry
            if bit % 2 == 0:  # even
                steps += 1
            else:  # odd → add 1 then divide by 2
                steps += 2
                carry = 1  # because adding 1 might cause carry

        return steps + carry
