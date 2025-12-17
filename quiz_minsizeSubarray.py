class Solution(object):
    def minSizeSubarray(self, nums, target):
        total_sum = sum(nums)
        n = len(nums)
        
        # Calculate the number of full arrays we can take
        count = (target // total_sum) * n
        target %= total_sum
        
        if target == 0:
            return count
            
        # To find the shortest subarray with sum 'target' (which is < total_sum),
        # we only need to check a window of size 2*n (simulating the infinite array wrapping once).
        nums = nums * 2
        min_len = float('inf')
        current_sum = 0
        left = 0
        
        for right, x in enumerate(nums):
            current_sum += x
            
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                min_len = min(min_len, right - left + 1)
                
        return -1 if min_len == float('inf') else count + min_len
