class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        # dp[i][j] stores the max dot product using subsequences of nums1[:i+1] and nums2[:j+1]
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                # Calculate dot product of current pair
                curr_product = nums1[i] * nums2[j]
                
                # Option 1: Start a new subsequence with just this pair
                dp[i][j] = curr_product
                
                # Option 2: Add this pair to a previous best subsequence (from i-1, j-1)
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + curr_product)
                
                # Option 3: Ignore nums1[i] (take best from nums1[:i], nums2[:j+1])
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                
                # Option 4: Ignore nums2[j] (take best from nums1[:i+1], nums2[:j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[n-1][m-1]
