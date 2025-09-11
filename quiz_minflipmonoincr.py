class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        flips = 0
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                flips = min(flips + 1, ones)
        return flips
