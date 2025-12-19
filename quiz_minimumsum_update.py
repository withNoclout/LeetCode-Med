class Solution(object):
    def minimumSum(self, nums):
        n = len(nums)
        if n < 3:
            return -1
        
        # Precompute minimums from the left
        left_min = [0] * n
        curr = float('inf')
        for i in range(n):
            curr = min(curr, nums[i])
            left_min[i] = curr
            
        right_min = float('inf')
        res = float('inf')
        
        # Iterate backwards to find peaks, maintaining right minimum
        for i in range(n - 2, 0, -1):
            right_min = min(right_min, nums[i+1])
            
            # Check mountain condition
            # left_min[i-1] is the minimum of nums[0...i-1]
            if left_min[i-1] < nums[i] and right_min < nums[i]:
                res = min(res, left_min[i-1] + nums[i] + right_min)
                
        return res if res != float('inf') else -1
