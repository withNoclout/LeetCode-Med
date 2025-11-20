class Solution(object):
    def maximumSum(self, nums):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        best = {}
        ans = -1

        for x in nums:
            s = digit_sum(x)
            if s in best:
                ans = max(ans, best[s] + x)
                if x > best[s]:
                    best[s] = x
            else:
                best[s] = x

        return ans
