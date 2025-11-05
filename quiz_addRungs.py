class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        prev = 0
        added = 0
        for r in rungs:
            gap = r - prev
            if gap > dist:
                added += (gap - 1) // dist
            prev = r
        return added
