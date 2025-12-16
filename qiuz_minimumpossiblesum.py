class Solution(object):
    def minimumPossibleSum(self, n, target):
        MOD = 10**9 + 7
        m = target // 2
        
        if n <= m:
            return (n * (n + 1) // 2) % MOD
            
        # Sum of 1 to m
        sum1 = m * (m + 1) // 2
        
        # Sum of n-m numbers starting from target
        rem = n - m
        last = target + rem - 1
        sum2 = rem * (target + last) // 2
        
        return (sum1 + sum2) % MOD
