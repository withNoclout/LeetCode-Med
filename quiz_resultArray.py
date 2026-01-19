class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # ans[x] will store the total count of subarrays with product % k == x
        ans = [0] * k
        
        # dp[r] stores the number of subarrays ending at the previous index
        # that have a product % k == r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            val = num % k
            
            # Case 1: The subarray consists of just the current number 'num'
            new_dp[val] += 1
            
            # Case 2: Extend existing subarrays ending at the previous position
            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * val) % k
                    new_dp[new_rem] += dp[r]
            
            # Add the counts ending at this position to the global answer
            for r in range(k):
                ans[r] += new_dp[r]
            
            # Update dp for the next iteration
            dp = new_dp
            
        return ans
