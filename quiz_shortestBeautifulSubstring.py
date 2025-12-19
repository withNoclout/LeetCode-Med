class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ones = [i for i, c in enumerate(s) if c == '1']
        if len(ones) < k:
            return ""
            
        res = ""
        for i in range(len(ones) - k + 1):
            sub = s[ones[i] : ones[i + k - 1] + 1]
            if not res or len(sub) < len(res) or (len(sub) == len(res) and sub < res):
                res = sub
                
        return res
