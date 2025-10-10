class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10**9 + 7
        lo, hi = 0, max(inventory)
        # Find smallest p such that sum(max(0, x - p)) <= orders
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 0
            for x in inventory:
                if x > mid:
                    cnt += x - mid
            if cnt > orders:
                lo = mid + 1
            else:
                hi = mid
        p = lo - 1  # threshold where values > p are counted

        total = 0
        cnt = 0
        for x in inventory:
            if x > p:
                m = x - p  # count of balls from p+1..x
                cnt += m
                # sum of arithmetic series from (p+1) to x
                total += (x + (p + 1)) * m // 2
        # remove extras at price (p+1)
        extra = cnt - orders
        total -= extra * (p + 1)
        return total % MOD
