class Solution(object):
    def rob(self, nums, colors):
        """
        :type nums: List[int]
        :type colors: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # prev2 represents dp[i-2] (max money ending 2 steps back)
        # prev1 represents dp[i-1] (max money ending 1 step back)
        prev2 = 0
        prev1 = nums[0]
        
        for i in range(1, n):
            current_val = nums[i]
            
            # Calculate the value if we choose to rob the current house 'i'
            rob_current = current_val
            
            if colors[i] != colors[i-1]:
                # If colors are different, the adjacent restriction does NOT apply.
                # We can combine the current house with the best sequence ending at i-1.
                rob_current += prev1
            else:
                # If colors are the same, we cannot rob i and i-1 together.
                # We must combine the current house with the best sequence ending at i-2.
                rob_current += prev2
            
            # The answer for step 'i' is the max of (Skipping i, Robbing i)
            current_max = max(prev1, rob_current)
            
            # Shift variables for the next iteration
            prev2 = prev1
            prev1 = current_max
            
        return prev1
