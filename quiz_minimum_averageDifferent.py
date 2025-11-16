class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        prefix = 0

        best_idx = 0
        best_val = float('inf')

        for i in range(n):
            prefix += nums[i]
            left_avg = prefix // (i + 1)
            if i == n - 1:
                right_avg = 0
            else:
                right_avg = (total - prefix) // (n - i - 1)
            diff = abs(left_avg - right_avg)
            if diff < best_val:
                best_val = diff
                best_idx = i

        return best_idx
