class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0  # min and max possible '(' count
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1      # treat '*' as ')'
                hi += 1      # or as '('
            if hi < 0:       # too many ')'
                return False
            if lo < 0:
                lo = 0       # can't go below 0 opens
        return lo == 0
