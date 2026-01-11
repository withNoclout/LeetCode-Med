class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minMaxSums(self, nums, k):
        n = len(nums)
        nums.sort()
        MOD = 10**9 + 7
        
        C = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, min(i, k) + 1):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
        
        sum_C = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            curr_sum = 0
            for j in range(k + 1):
                curr_sum = (curr_sum + C[i][j]) % MOD
                sum_C[i][j] = curr_sum

        ans = 0
        for i in range(n):
            # As Minimum: choosing from n-1-i larger elements
            ways_min = sum_C[n - 1 - i][min(n - 1 - i, k - 1)]
            # As Maximum: choosing from i smaller elements
            ways_max = sum_C[i][min(i, k - 1)]
            
            ans = (ans + nums[i] * (ways_min + ways_max)) % MOD
            
        return ans
