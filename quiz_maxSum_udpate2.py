class Solution(object):
    def maxSum(self, nums, m, k):
        import collections
        counts = collections.defaultdict(int)
        current_sum = 0
        max_sum = 0
        
        # Initialize first window
        for i in range(k):
            counts[nums[i]] += 1
            current_sum += nums[i]
            
        if len(counts) >= m:
            max_sum = current_sum
            
        # Slide window
        for i in range(k, len(nums)):
            counts[nums[i]] += 1
            current_sum += nums[i]
            
            remove_val = nums[i-k]
            counts[remove_val] -= 1
            current_sum -= remove_val
            
            if counts[remove_val] == 0:
                del counts[remove_val]
                
            if len(counts) >= m:
                max_sum = max(max_sum, current_sum)
                
        return max_sum
