class Solution(object):
    def minimumSubstringsInPartition(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            count = {}
            max_freq = 0
            for j in range(i, 0, -1):
                char = s[j-1]
                count[char] = count.get(char, 0) + 1
                max_freq = max(max_freq, count[char])
                
                if max_freq * len(count) == i - j + 1:
                    dp[i] = min(dp[i], dp[j-1] + 1)
                    
        return dp[n]
