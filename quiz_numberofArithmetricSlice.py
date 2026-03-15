from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_count = 0
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # The number of subsequences ending at j with difference diff
                count = dp[j][diff]
                
                # Each of these can be extended to form a valid slice of length >= 3
                total_count += count
                
                # Add the extended sequences and the new length 2 sequence [nums[j], nums[i]]
                dp[i][diff] += count + 1
                
        return total_count
