class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        memo = {}

        def dp(i, num):
            if i >= n:
                return num
            if i == n - 1:
                return max(nums[i], num)

            state = (i, num)
            if state in memo:
                return memo[state]

            # Sort the three candidates: the carry-over 'num' and the next pair
            candidates = [num, nums[i], nums[i+1]]
            candidates.sort()
            lo, md, hi = candidates[0], candidates[1], candidates[2]

            # Logic based on the sorted triad:
            # 1. Keep 'lo' -> remove (md, hi), cost is max(md, hi) = hi
            # 2. Keep 'md' -> remove (lo, hi), cost is max(lo, hi) = hi
            # 3. Keep 'hi' -> remove (lo, md), cost is max(lo, md) = md
            res = min(hi + dp(i + 2, lo), 
                      hi + dp(i + 2, md), 
                      md + dp(i + 2, hi))
            
            memo[state] = res
            return res

        return dp(1, nums[0])
