class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Single pass, O(n) time, O(1) space.
        # Track lengths of the current increasing run and the previous run.
        ans = 0
        inc = 1
        prev_inc = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                prev_inc = inc
                inc = 1
            # Case 1: both subarrays lie inside one long run (split in the middle)
            ans = max(ans, inc // 2)
            # Case 2: subarrays lie on two adjacent runs (split at the boundary)
            ans = max(ans, min(prev_inc, inc))

        return ans
