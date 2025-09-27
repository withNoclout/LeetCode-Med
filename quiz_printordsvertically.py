class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        max_len = max(len(w) for w in words)
        res = []

        for i in range(max_len):
            col = []
            for w in words:
                if i < len(w):
                    col.append(w[i])
                else:
                    col.append(" ")
            res.append("".join(col).rstrip())
        return res
