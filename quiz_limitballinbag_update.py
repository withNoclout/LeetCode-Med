class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            ops = 0
            for x in nums:
                ops += (x - 1) // mid
            if ops > maxOperations:
                left = mid + 1
            else:
                right = mid
        return left
