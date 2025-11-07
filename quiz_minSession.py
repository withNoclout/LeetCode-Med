class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        full = 1 << n
        INF = float('inf')

        # Precompute total time for each subset
        subset_sum = [0] * full
        for mask in range(full):
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += tasks[i]
            subset_sum[mask] = total

        dp = [INF] * full
        dp[0] = 0

        # DP over all subsets
        for mask in range(full):
            sub = mask
            while sub:
                if subset_sum[sub] <= sessionTime:
                    dp[mask] = min(dp[mask], dp[mask ^ sub] + 1)
                sub = (sub - 1) & mask

        return dp[full - 1]
