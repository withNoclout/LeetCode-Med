class Solution(object):
    def countSubstrings(self, s, c):
        n = s.count(c)
        return n * (n + 1) // 2
