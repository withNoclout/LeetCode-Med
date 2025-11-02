import math

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        n = len(dist)
        if hour <= n - 1:
            return -1

        def time_needed(speed):
            total = 0
            for d in dist[:-1]:
                total += math.ceil(float(d) / speed)
            total += float(dist[-1]) / speed
            return total

        left, right = 1, 10**7
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if time_needed(mid) <= hour:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
