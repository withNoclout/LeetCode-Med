class Solution(object):
    def addSpaces(self, s, spaces):
        res = []
        prev = 0
        for sp in spaces:
            res.append(s[prev:sp])
            res.append(' ')
            prev = sp
        res.append(s[prev:])
        return ''.join(res)
