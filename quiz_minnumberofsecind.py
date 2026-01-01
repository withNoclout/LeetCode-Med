import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        def check(t):
            total_h = 0
            for w in workerTimes:
                # Calculate max height x for this worker within time t
                # Cost = w * x * (x + 1) / 2 <= t
                # 2t/w >= x^2 + x
                # Quadratic formula positive root: x = (-1 + sqrt(1 + 8t/w)) / 2
                val = 1 + 8 * t // w
                x = int((math.sqrt(val) - 1) / 2)
                total_h += x
                if total_h >= mountainHeight:
                    return True
            return False

        min_w = min(workerTimes)
        # Upper bound: fast worker does it all alone
        high = min_w * mountainHeight * (mountainHeight + 1) // 2
        low = 1
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
