class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def find_divisors(n):
            import math
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]

        cand1 = find_divisors(num + 1)
        cand2 = find_divisors(num + 2)

        # choose the pair with minimal abs difference
        if abs(cand1[0] - cand1[1]) < abs(cand2[0] - cand2[1]):
            return cand1
        else:
            return cand2
