class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10**9 + 7
        count = 0
        res = 0

        for ch in s:
            if ch == '1':
                count += 1
                res = (res + count) % mod
            else:
                count = 0

        return res
