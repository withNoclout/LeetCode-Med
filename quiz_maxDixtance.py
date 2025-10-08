class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        def canPlace(dist):
            count = 1
            last = position[0]
            for p in position[1:]:
                if p - last >= dist:
                    count += 1
                    last = p
                if count >= m:
                    return True
            return False

        left, right = 1, position[-1] - position[0]
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if canPlace(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
