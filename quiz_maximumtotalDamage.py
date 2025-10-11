class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(power)
        vals = sorted(cnt.keys())
        dmg = [v * cnt[v] for v in vals]
        n = len(vals)
        dp = [0] * (n + 1)

        j = 0
        for i in range(1, n + 1):
            # Move j to first index where vals[i-1] - vals[j] > 2 (non-conflicting)
            while j < i and vals[i - 1] - vals[j] > 2:
                j += 1
            non_conflict_idx = j  # dp index corresponds to j
            take = dmg[i - 1] + dp[non_conflict_idx]
            skip = dp[i - 1]
            dp[i] = max(skip, take)

        return dp[n]
