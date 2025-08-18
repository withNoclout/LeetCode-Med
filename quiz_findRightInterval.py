class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        import bisect

        n = len(intervals)
        starts = sorted((intervals[i][0], i) for i in range(n))
        res = [-1] * n

        for i, (s, e) in enumerate(intervals):
            idx = bisect.bisect_left(starts, (e, ))
            if idx < n:
                res[i] = starts[idx][1]

        return res
