class Solution(object):
    def maximumSubarraySum(self, nums, k):
        res = 0
        curr = 0
        count = {}
        
        for i, num in enumerate(nums):
            curr += num
            count[num] = count.get(num, 0) + 1
            
            if i >= k:
                left = nums[i - k]
                curr -= left
                count[left] -= 1
                if count[left] == 0:
                    del count[left]
            
            if len(count) == k:
                res = max(res, curr)
                
        return res
