class Solution(object):
    def minimumOperations(self, nums):
        # dp1: min ops to make sequence non-decreasing ending with 1
        # dp2: min ops to make sequence non-decreasing ending with 2
        # dp3: min ops to make sequence non-decreasing ending with 3
        dp1 = dp2 = dp3 = 0
        
        for x in nums:
            # To end with 1: must come from previous 1. Cost +1 if current != 1.
            dp1 += (1 if x != 1 else 0)
            
            # To end with 2: can come from 1 or 2. Cost +1 if current != 2.
            # We take min(prev_dp1, prev_dp2) because we can transition from 1 to 2.
            dp2 = min(dp1 - (1 if x != 1 else 0), dp2) + (1 if x != 2 else 0)
            
            # To end with 3: can come from 1, 2, or 3. Cost +1 if current != 3.
            dp3 = min(dp1 - (1 if x != 1 else 0), dp2 - (1 if x != 2 else 0), dp3) + (1 if x != 3 else 0)
            
        return min(dp1, dp2, dp3)
