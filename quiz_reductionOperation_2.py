class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        ops = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ops += 1
            res += ops
        return res
