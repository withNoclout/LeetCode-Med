

class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        stack = []
        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                num = lcm(stack.pop(), num)
            stack.append(num)
        return stack
