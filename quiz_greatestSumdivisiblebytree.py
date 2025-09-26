class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]
        for x in nums:
            new_dp = dp[:]
            for r in range(3):
                nr = (r + x) % 3
                new_dp[nr] = max(new_dp[nr], dp[r] + x)
            dp = new_dp
        return dp[0]
