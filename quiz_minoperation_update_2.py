from math import gcd

class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones

        best = float('inf')
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        if best == float('inf'):
            return -1
        return (best - 1) + (n - 1)
