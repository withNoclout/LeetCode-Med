class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        import math
        times = [math.ceil(d / s) for d, s in zip(dist, speed)]
        times.sort()

        for i, t in enumerate(times):
            if t <= i:
                return i
        return len(times)
