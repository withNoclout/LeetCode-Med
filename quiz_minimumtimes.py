class Solution(object):
    def minimumTime(self, time, totalTrips):
        left, right = 1, min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            trips = 0
            for t in time:
                trips += mid // t
                if trips >= totalTrips:
                    break
            if trips >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left
