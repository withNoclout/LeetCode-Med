class Solution(object):
    def maxSumDivThree(self, nums):
        dp = [0, 0, 0]
        for num in nums:
            for x in dp[:]:
                dp[(x + num) % 3] = max(dp[(x + num) % 3], x + num)
        return dp[0]
