class Solution(object):
    def specialTriplets(self, nums):
        import collections
        left = collections.defaultdict(int)
        right = collections.Counter(nums)
        
        res = 0
        MOD = 10**9 + 7
        
        for x in nums:
            right[x] -= 1
            target = x * 2
            
            # Check for nums[i] == nums[j] * 2 and nums[k] == nums[j] * 2
            # where i < j < k. Current x is nums[j].
            if left[target] > 0 and right[target] > 0:
                res = (res + left[target] * right[target]) % MOD
                
            left[x] += 1
            
        return res
