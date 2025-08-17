class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        
        return dp[target]
