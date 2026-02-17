class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # 1. Precompute Suffix Minimums
        # right_min[k] will store min(nums[k:])
        right_min = [0] * n
        right_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i+1])
            
        max_score = float('-inf')
        current_prefix_sum = 0
        
        # 2. Iterate through valid split indices
        # Valid split index i is from 0 to n-2 (leaving at least one element for suffix)
        for i in range(n - 1):
            current_prefix_sum += nums[i]
            
            # The suffix part is nums[i+1:], so its minimum is stored at right_min[i+1]
            current_suffix_min = right_min[i+1]
            
            current_score = current_prefix_sum - current_suffix_min
            
            if current_score > max_score:
                max_score = current_score
                
        return max_score
