class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        import itertools
        max_time = -1
        for h1, h2, m1, m2 in itertools.permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if 0 <= hour < 24 and 0 <= minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        if max_time == -1:
            return ""
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
