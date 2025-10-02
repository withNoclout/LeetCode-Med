class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur = 1
        for num in target:
            while cur < num:
                res.append("Push")
                res.append("Pop")
                cur += 1
            res.append("Push")
            cur += 1
        return res
