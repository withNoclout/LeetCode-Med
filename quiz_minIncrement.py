class Solution(object):
    def minIncrements(self, n, cost):
        res = 0
        for i in range(n // 2, 0, -1):
            left = 2 * i - 1
            right = 2 * i
            res += abs(cost[left] - cost[right])
            cost[i - 1] += max(cost[left], cost[right])
        return res
