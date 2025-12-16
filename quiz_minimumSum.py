class Solution(object):
    def minimumSum(self, n, k):
        m = k // 2
        if n <= m:
            return n * (n + 1) // 2
        
        # Sum of 1 to m
        part1 = m * (m + 1) // 2
        
        # Sum of n-m terms starting from k
        count = n - m
        part2 = count * (2 * k + (count - 1)) // 2
        
        return part1 + part2
