class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def kadane(nums):
            best = cur = 0
            for x in nums:
                cur = max(x, cur + x)
                best = max(best, cur)
            return best

        total = sum(arr)
        if k == 1:
            return kadane(arr) % MOD

        # For k >= 2, consider arr twice
        best_two = kadane(arr * 2)
        if total > 0:
            return (best_two + (k - 2) * total) % MOD
        else:
            return best_two % MOD
