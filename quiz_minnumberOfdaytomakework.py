class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1

        def canMake(day):
            bouquets = 0
            flowers = 0
            for d in bloomDay:
                if d <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False

        left, right = min(bloomDay), max(bloomDay)
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
