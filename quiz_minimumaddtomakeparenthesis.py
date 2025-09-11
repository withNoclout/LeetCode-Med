class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance == 0:
                    res += 1
                else:
                    balance -= 1
        return res + balance
