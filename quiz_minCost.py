class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        sr, sc = startPos
        tr, tc = homePos
        cost = 0

        # Move rows
        step = 1 if sr < tr else -1
        r = sr
        while r != tr:
            r += step
            cost += rowCosts[r]

        # Move cols
        step = 1 if sc < tc else -1
        c = sc
        while c != tc:
            c += step
            cost += colCosts[c]

        return cost
