class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 3:
            return 0

        index = {v: i for i, v in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        ans = 0

        for k in range(n):
            for j in range(k):
                i = index.get(arr[k] - arr[j])
                if i is not None and i < j:
                    dp[j][k] = dp[i][j] + 1
                    ans = max(ans, dp[j][k])

        return ans if ans >= 3 else 0
