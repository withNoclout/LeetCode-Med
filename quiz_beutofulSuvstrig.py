class Solution(object):
    def beautifulSubstrings(self, s, k):
        vowels = set('aeiou')
        res = 0
        n = len(s)
        for i in range(n):
            v = c = 0
            for j in range(i, n):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1
                
                if v == c and (v * c) % k == 0:
                    res += 1
        return res
