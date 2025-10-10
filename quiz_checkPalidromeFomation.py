class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def is_pal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def check(x, y):
            i, j = 0, len(x) - 1
            while i < j and x[i] == y[j]:
                i += 1
                j -= 1
            return is_pal(x, i, j) or is_pal(y, i, j)

        return check(a, b) or check(b, a)
