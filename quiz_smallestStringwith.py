class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Start with all 'a' => total value n
        res = ['a'] * n
        remain = k - n
        i = n - 1
        while remain > 0 and i >= 0:
            add = min(25, remain)  # can upgrade 'a' by at most 25 to reach 'z'
            res[i] = chr(ord('a') + add)
            remain -= add
            i -= 1
        return ''.join(res)
