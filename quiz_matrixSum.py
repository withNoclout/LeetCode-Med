class Solution(object):
    def matrixSum(self, nums):
        for row in nums:
            row.sort()
        return sum(max(col) for col in zip(*nums))
