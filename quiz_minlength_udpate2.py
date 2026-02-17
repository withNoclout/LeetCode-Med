from collections import defaultdict

class Solution(object):
    def minLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = defaultdict(int)
        distinct_sum = 0
        left = 0
        min_len = float('inf')
        n = len(nums)
        
        for right in range(n):
            # 1. Expand the window by adding nums[right]
            val = nums[right]
            counts[val] += 1
            
            # If this is the first occurrence in the current window, add to sum
            if counts[val] == 1:
                distinct_sum += val
            
            # 2. Shrink the window from the left as long as the condition is met
            while distinct_sum >= k:
                # Update minimum length found so far
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                
                # Remove nums[left] from the window
                left_val = nums[left]
                counts[left_val] -= 1
                
                # If count drops to 0, this distinct value is completely gone
                if counts[left_val] == 0:
                    distinct_sum -= left_val
                
                left += 1
                
        return min_len if min_len != float('inf') else -1
