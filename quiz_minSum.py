class Solution(object):
    def minArraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # Prefix sum array (pref[i] is sum of nums[0...i-1])
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]

        # dp[i] stores the maximum sum we can remove from the first i elements
        dp = [0] * (n + 1)
        
        # last_idx[mod] stores the most recent index 'j' such that pref[j] % k == mod
        last_idx = {}
        last_idx[0] = 0

        for i in range(1, n + 1):
            # Option 1: Do not include the subarray ending at i in the deletion set
            dp[i] = dp[i-1]
            
            # Calculate current prefix remainder
            current_mod = pref[i] % k
            
            # Option 2: If we found a previous prefix with the same remainder,
            # the subarray between them is divisible by k.
            # Try to combine the deleted sum up to 'prev' + the new subarray sum.
            if current_mod in last_idx:
                prev = last_idx[current_mod]
                subarray_sum = pref[i] - pref[prev]
                dp[i] = max(dp[i], dp[prev] + subarray_sum)
            
            # Update the last seen index for this remainder
            last_idx[current_mod] = i

        # The result is Total Sum - Maximum Deletable Sum
        return pref[n] - dp[n]
