class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort items by price and build prefix max beauty
        items.sort()
        prices = []
        pref = []
        mx = 0
        for p, b in items:
            mx = max(mx, b)
            prices.append(p)
            pref.append(mx)

        # Answer each query with binary search on prices
        import bisect
        res = []
        for q in queries:
            i = bisect.bisect_right(prices, q) - 1
            res.append(pref[i] if i >= 0 else 0)
        return res
