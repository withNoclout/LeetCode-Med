class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total0 = s.count('0')
        total1 = n - total0

        left0 = left1 = 0
        ways = 0

        for ch in s:
            if ch == '0':
                # as middle '0', pairs are (1,_ ,0) and (0,_ ,1) patterns
                ways += left1 * (total1 - left1)
                left0 += 1
            else:  # ch == '1'
                ways += left0 * (total0 - left0)
                left1 += 1

        return ways
