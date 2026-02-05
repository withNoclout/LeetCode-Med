class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_n = max(nums)
        # Handle edge case where array only contains 0s
        if max_n == 0:
            return 0
            
        # Calculate max_mask (equivalent to (1 << (msb + 1)) - 1)
        # This creates a mask of all 1s covering the bit_length of max_n
        msb = max_n.bit_length() - 1
        max_mask = (1 << (msb + 1)) - 1
        
        # Initialize DP table
        # dp[mask] will store the maximum value 'x' from nums such that 'x' is a submask of 'mask'
        dp = [0] * (max_mask + 1)
        for x in nums:
            dp[x] = x
            
        # SOS DP (Sum Over Subsets) Propagation
        # Iterate through each bit position 'b'
        for b in range(msb + 1):
            bit = 1 << b
            # Iterate through all masks
            for mask in range(max_mask + 1):
                if mask & bit:
                    dp[mask] = max(dp[mask], dp[mask ^ bit])
                    
        ans = 0
        for n in nums:
            # We need a number 'm' such that (n & m) == 0.
            # This means 'm' must be a submask of the complement of 'n'.
            complement = max_mask ^ n
            ans = max(ans, n * dp[complement])
            
        return anso

