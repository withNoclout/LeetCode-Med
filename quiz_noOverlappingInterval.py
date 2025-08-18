class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # sort by end time
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1  # overlap, remove one
            else:
                end = intervals[i][1]

        return count

