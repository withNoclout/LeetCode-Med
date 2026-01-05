class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        res = []
        curr = []
        for char in target:
            curr.append('a')
            res.append("".join(curr))
            while curr[-1] != char:
                curr[-1] = chr(ord(curr[-1]) + 1)
                res.append("".join(curr))
        return res
