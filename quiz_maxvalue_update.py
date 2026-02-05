class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        
        # Step 1: Precompute Prefix Maximums
        # pre_max[i] stores the maximum value in nums[0...i]
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], nums[i])
            
        # Step 2: Traverse backwards maintaining Suffix Minimum
        # suf_min stores the minimum value seen so far in the suffix nums[i+1...n-1]
        suf_min = float('inf')
        
        for i in range(n - 1, -1, -1):
            # If the max value to the left (including self) is greater than the min value to the right,
            # we can bridge the gap to reach the same maximums reachable from the right side.
            if pre_max[i] > suf_min:
                ans[i] = ans[i+1]
            else:
                # Otherwise, the best we can guarantee is the current prefix max
                ans[i] = pre_max[i]
            
            # Update suffix minimum for the next iteration
            if nums[i] < suf_min:
                suf_min = nums[i]
                
        return ans
