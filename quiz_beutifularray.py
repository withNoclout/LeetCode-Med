class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [1]
        while len(res) < n:
            res = [x * 2 - 1 for x in res] + [x * 2 for x in res]
        return [x for x in res if x <= n]
