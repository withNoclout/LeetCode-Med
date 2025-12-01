class Solution(object):
    def maximumOr(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] | nums[i]
            
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i+1] | nums[i]
            
        res = 0
        for i in range(n):
            res = max(res, prefix[i] | (nums[i] << k) | suffix[i+1])
            
        return res
