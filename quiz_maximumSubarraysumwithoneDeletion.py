class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 0:
            return 0
        # dp0 = max subarray sum ending at i with no deletion
        # dp1 = max subarray sum ending at i with one deletion
        dp0 = arr[0]
        dp1 = float('-inf')
        ans = arr[0]
        for i in range(1, n):
            dp1 = max(dp0, dp1 + arr[i])     # either delete current, or extend previous with deletion
            dp0 = max(dp0 + arr[i], arr[i])  # extend or start new
            ans = max(ans, dp0, dp1)
        return ans
