import math

class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0, int(math.isqrt(c))  # isqrt avoids floating-point issues
        while left <= right:
            s = left * left + right * right
            if s == c:
                return True
            elif s < c:
                left += 1
            else:
                right -= 1
        return False
