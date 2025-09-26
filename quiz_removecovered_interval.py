class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by start asc, and if equal then by end desc
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        prev_end = 0
        for _, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end
        return count

