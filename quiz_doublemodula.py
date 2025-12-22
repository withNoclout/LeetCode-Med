class Solution(object):
    def getGoodIndices(self, variables, target):
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            if pow(pow(a, b, 10), c, m) == target:
                res.append(i)
        return res
