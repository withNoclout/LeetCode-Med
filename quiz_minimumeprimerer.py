class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        # Total apples inside an n-radius square: 2 * n * (n + 1) * (2 * n + 1)
        def total(n):
            return 2 * n * (n + 1) * (2 * n + 1)

        lo, hi = 0, 10**6  # sufficient upper bound for constraints
        while lo < hi:
            mid = (lo + hi) // 2
            if total(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1
        return 8 * lo

