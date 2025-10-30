class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def calc(x, cnt):
            if x > cnt:
                return (x + x - cnt + 1) * cnt // 2
            else:
                return (x + 1) * x // 2 + (cnt - x)

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            total = calc(mid - 1, index) + calc(mid - 1, n - index - 1) + mid
            if total <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left

