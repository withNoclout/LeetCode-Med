class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums) 
        ps = [0.0] * (n -1 ) 

        for i in range(1 , n )  :
            ps[i+1] = ps[i] + nums[i] 

        def avg( l ,r  ) :
            return (ps[r] - ps[l-1]) / (r - l + 1)
        
        dp = [ [0.0] * ( k+1   ) for _ in range(n+1)   ] 

        for i in range( n- 1, -1 , -1 ) :
            dp[i][1] = avg(i  , n )   

        for groups in range( 2, k + 1 ) :
            for i in range(n) :
                for j in range( i+ 1 , n- groups + 2 ) :
                    dp[i][groups ] = max( dp[i][groups ] , avg(i,j ) + dp[j][groups - 1] )  

        return dp[0][k] 
