class Solution(object):
    def maximumLength(self, nums, k):
        n = len(nums)
        dp = [[1] * (k + 1) for _ in range(n)]
        res = 1
        
        for i in range(n):
            for j in range(k + 1):
                for p in range(i):
                    if nums[i] == nums[p]:
                        dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[p][j-1] + 1)
                res = max(res, dp[i][j])
                
        return res
