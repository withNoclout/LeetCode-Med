class Solution(object):
    def minimumK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary search for the minimum k.
        # Range: [1, sufficiently_large_number]
        # A safe upper bound is max(max(nums), len(nums)).
        low = 1
        high = max(nums) + len(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid == 0: # Safety check, though low starts at 1
                low = 1
                continue
            
            # Calculate the total operations needed with divisor 'mid'
            current_ops = 0
            limit = mid * mid
            
            possible = True
            for x in nums:
                # Calculate ceil(x / mid) using integer math
                current_ops += (x + mid - 1) // mid
                
                # Optimization: If ops exceed limit early, stop
                if current_ops > limit:
                    possible = False
                    break
            
            if possible:
                # If valid, try a smaller k
                ans = mid
                high = mid - 1
            else:
                # If not valid (ops > k^2), we need a larger k to reduce ops and increase k^2
                low = mid + 1
                
        return ans
