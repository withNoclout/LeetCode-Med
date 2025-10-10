class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = [0]*n
        ans = float('-inf')
        for i in range(n-1, -1, -1):
            dp[i] = energy[i]
            if i + k < n and dp[i + k] > 0:
                dp[i] += dp[i + k]
            if dp[i] > ans:
                ans = dp[i]
        return ans
