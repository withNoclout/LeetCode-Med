class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        import collections
        # Transform nums to 1 if nums[i] % modulo == k else 0
        prefix_sum = 0
        count = collections.defaultdict(int)
        count[0] = 1  # Base case for prefix sum
        res = 0
        
        for x in nums:
            # Check condition: nums[i] % modulo == k
            val = 1 if x % modulo == k else 0
            prefix_sum = (prefix_sum + val) % modulo
            
            # We want (prefix_sum[i] - prefix_sum[j]) % modulo == k
            # prefix_sum[j] = (prefix_sum[i] - k) % modulo
            target = (prefix_sum - k) % modulo
            res += count[target]
            
            count[prefix_sum] += 1
            
        return res
