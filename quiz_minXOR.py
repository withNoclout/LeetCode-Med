class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def minXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # 1. Build Prefix XOR array
        # prefix[i] stores XOR of nums[0]...nums[i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ nums[i]
            
        # 2. Initialize DP table
        # dp[j][i] = min-max XOR for partitioning first i elements into j groups
        inf = float('inf')
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        
        # Base case: 0 elements into 0 groups has cost 0
        dp[0][0] = 0
        
        # 3. Fill DP Table
        # j: current number of partitions (1 to k)
        for j in range(1, k + 1):
            # i: current end index of the array prefix (j to n)
            # We need at least j elements to form j partitions
            for i in range(j, n + 1):
                # p: split point where the last subarray starts (p to i-1)
                # The previous j-1 partitions use elements up to p
                for p in range(j - 1, i):
                    current_sub_xor = prefix[i] ^ prefix[p]
                    current_cost = max(dp[j-1][p], current_sub_xor)
                    
                    if current_cost < dp[j][i]:
                        dp[j][i] = current_cost
                        
        return dp[k][n]
