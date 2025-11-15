class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        # Binary search for the maximum candies per child
        left, right = 1, max(candies)
        ans = 0

        def can(x):
            count = 0
            for c in candies:
                count += c // x
                if count >= k:
                    return True
            return False

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
