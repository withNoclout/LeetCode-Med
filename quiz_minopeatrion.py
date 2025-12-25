class Solution(object):
    def minOperations(self, k):
        res = k
        for x in range(1, k + 1):
            ops = (x - 1) + (k - 1) // x
            res = min(res, ops)
            if x * x >= k:
                break
        return res
