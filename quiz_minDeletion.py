class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        deletions = 0
        i = 0

        while i < n - 1:
            if nums[i] == nums[i + 1]:
                deletions += 1
                i += 1
            else:
                i += 2

        if (n - deletions) % 2 == 1:
            deletions += 1

        return deletions

