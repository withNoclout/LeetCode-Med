class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_four_divisors_sum(x):
            divisors = set()
            for i in range(1, int(x ** 0.5) + 1):
                if x % i == 0:
                    divisors.add(i)
                    divisors.add(x // i)
                if len(divisors) > 4:
                    return 0
            return sum(divisors) if len(divisors) == 4 else 0

        total = 0
        for num in nums:
            total += get_four_divisors_sum(num)
        return total
