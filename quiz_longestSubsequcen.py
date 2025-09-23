class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp= {} 
        ans = 0 
        for x in arr  :
            dp[x] = dp.get( x - difference ,  0 ) + 1 
            ans = max( ans  , dp[x]  ) 

        return ans 
