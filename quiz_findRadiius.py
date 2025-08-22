import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        res = 0

        for house in houses:
            idx = bisect.bisect_left(heaters, house)

            left = float('inf') if idx == 0 else house - heaters[idx - 1]
            right = float('inf') if idx == len(heaters) else heaters[idx] - house

            res = max(res, min(left, right))

        return res
