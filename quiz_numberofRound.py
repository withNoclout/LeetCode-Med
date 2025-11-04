class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        h1, m1 = map(int, loginTime.split(':'))
        h2, m2 = map(int, logoutTime.split(':'))
        start = h1 * 60 + m1
        end = h2 * 60 + m2
        if end < start:
            end += 24 * 60

        start = (start + 14) // 15 * 15
        end = end // 15 * 15
        return max(0, (end - start) // 15)
