class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if not piles:
            return 0

        lo, hi = 1, max(piles)

        def hours_needed(k):
            total = 0
            for p in piles:
                # ceil division
                total += (p + k - 1) // k
                if total > h:
                    break
            return total

        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo
# ...existing code...
