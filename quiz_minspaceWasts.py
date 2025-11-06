class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        INF = 10**18

        # cost[i][j]: waste if we choose one segment covering nums[i..j]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            mx = 0
            s = 0
            for j in range(i, n):
                mx = max(mx, nums[j])
                s += nums[j]
                cost[i][j] = mx * (j - i + 1) - s

        # dp_prev[p]: minimal waste to partition first p elements with current number of segments used
        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0

        # With k resizes we can have up to k+1 segments.
        for _ in range(k + 1):
            dp_cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                best = INF
                for p in range(i):
                    best = min(best, dp_prev[p] + cost[p][i - 1])
                dp_cur[i] = best
            dp_prev = dp_cur

        return dp_prev[n]
