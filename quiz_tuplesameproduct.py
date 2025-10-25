class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        prod_count = Counter()

        # count frequency of each pair product
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                prod_count[nums[i] * nums[j]] += 1

        res = 0
        # for each product that occurs c times,
        # we can form c choose 2 combinations
        # each contributes 8 valid tuples
        for c in prod_count.values():
            if c > 1:
                res += 8 * c * (c - 1) // 2

        return res
