class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add_ops = 0
        max_bits = 0

        for num in nums:
            bits = 0
            while num > 0:
                if num % 2 == 1:
                    add_ops += 1
                num //= 2
                bits += 1
            max_bits = max(max_bits, bits)

        return add_ops + max_bits - 1
