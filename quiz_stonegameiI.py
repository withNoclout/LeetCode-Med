class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        # suffix sums
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, m):
            if i >= n:
                return 0
            if 2 * m >= n - i:
                return suffix[i]
            best = 0
            for x in range(1, 2 * m + 1):
                best = max(best, suffix[i] - dp(i + x, max(m, x)))
            return best

        return dp(0, 1)
