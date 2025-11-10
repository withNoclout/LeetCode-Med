class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        def can(x):
            # number of stores needed if each store holds at most x items
            need = 0
            for q in quantities:
                need += (q + x - 1) // x
                if need > n:
                    return False
            return need <= n

        lo, hi = 1, max(quantities)
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
