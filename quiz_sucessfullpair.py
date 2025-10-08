import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        n = len(potions)
        res = []
        for s in spells:
            min_potion = float(success) / s
            idx = bisect.bisect_left(potions, min_potion)
            res.append(n - idx)
        return res
