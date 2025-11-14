class Solution(object):
    def maximumEvenSplit(self, finalSum):
        if finalSum % 2 == 1:
            return []
        res = []
        cur = 2
        rem = finalSum
        while rem >= cur:
            res.append(cur)
            rem -= cur
            cur += 2
        if rem > 0:
            res[-1] += rem
        return res
