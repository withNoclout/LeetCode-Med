class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        dp = [1] * n
        parent = [-1] * n
        
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    diff = 0
                    for c1, c2 in zip(words[i], words[j]):
                        if c1 != c2: diff += 1
                        if diff > 1: break
                    if diff == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            parent[i] = j
                            
        max_idx = 0
        for i in range(n):
            if dp[i] > dp[max_idx]:
                max_idx = i
                
        res = []
        curr = max_idx
        while curr != -1:
            res.append(words[curr])
            curr = parent[curr]
            
        return res[::-1]
